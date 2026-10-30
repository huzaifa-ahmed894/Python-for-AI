import os, json, sqlite3, datetime
from functools import wraps
from flask import Flask, g, jsonify, request, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("DB_PATH", os.path.join(BASE, "lms.db"))
MAX_CREDITS = 18
app = Flask(__name__, static_folder="static", static_url_path="")
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")

SCHEMA = """
CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, sid TEXT UNIQUE, name TEXT, password_hash TEXT, program TEXT, semester INTEGER);
CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY, code TEXT, title TEXT, instructor TEXT, credits INTEGER, capacity INTEGER, days TEXT, start INTEGER, end INTEGER, room TEXT);
CREATE TABLE IF NOT EXISTS enrollments(student_id INTEGER, course_id INTEGER, PRIMARY KEY(student_id, course_id));
CREATE TABLE IF NOT EXISTS waitlist(student_id INTEGER, course_id INTEGER, PRIMARY KEY(student_id, course_id));
CREATE TABLE IF NOT EXISTS deadlines(id INTEGER PRIMARY KEY, course_id INTEGER, title TEXT, due TEXT);
CREATE TABLE IF NOT EXISTS notices(id INTEGER PRIMARY KEY, title TEXT, created TEXT);
CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY, student_id INTEGER, answers TEXT, created TEXT);
"""

def init_db():
    c = sqlite3.connect(DB)
    c.executescript(SCHEMA)
    if not c.execute("SELECT 1 FROM students").fetchone():
        pw = generate_password_hash("student123")
        c.executemany("INSERT INTO students(sid,name,password_hash,program,semester) VALUES(?,?,?,?,?)", [
            ("24F-CS-001", "Ayesha Khan", pw, "BS Computer Science", 5),
            ("24F-CS-002", "Bilal Ahmed", pw, "BS Computer Science", 5)])
        courses = [
            ("CS-301", "Human Computer Interaction", "Dr. Sana Malik", 3, 30, "Mon,Wed", 540, 630, "Lab 2"),
            ("CS-302", "Database Systems", "Dr. Omar Farooq", 3, 30, "Mon,Wed", 660, 750, "Room 14"),
            ("CS-303", "Operating Systems", "Dr. Hina Riaz", 3, 30, "Tue,Thu", 540, 630, "Room 9"),
            ("CS-304", "Software Engineering", "Dr. Kamran Ali", 3, 30, "Tue,Thu", 660, 750, "Room 11"),
            ("CS-305", "Computer Networks", "Dr. Zara Hussain", 3, 25, "Mon,Wed", 840, 930, "Room 7"),
            ("CS-306", "Artificial Intelligence", "Dr. Imran Sheikh", 3, 1, "Tue,Thu", 840, 930, "Lab 1"),
            ("MT-201", "Probability and Statistics", "Dr. Nida Qureshi", 3, 30, "Fri", 540, 720, "Room 3"),
            ("CS-307", "Web Engineering", "Dr. Faraz Mirza", 3, 30, "Mon,Wed", 570, 660, "Lab 3"),
            ("HU-101", "Technical Writing", "Ms. Rabia Noor", 2, 30, "Fri", 780, 900, "Room 5"),
            ("CS-308", "Mobile App Development", "Dr. Saad Baig", 3, 30, "Tue,Thu", 960, 1050, "Lab 4"),
            ("CS-309", "Data Structures and Algorithms", "Dr. Ayaz Memon", 3, 35, "Mon,Wed", 930, 1020, "Room 12"),
            ("CS-310", "Cyber Security", "Dr. Mehwish Tariq", 3, 30, "Tue,Thu", 780, 870, "Room 6"),
            ("CS-311", "Machine Learning", "Dr. Adeel Raza", 3, 30, "Fri", 930, 1110, "Lab 5"),
            ("CS-312", "Cloud Computing", "Dr. Sumaira Jamal", 3, 30, "Mon,Wed", 1020, 1110, "Room 8"),
            ("CS-313", "Computer Graphics", "Dr. Yusuf Lakhani", 3, 3, "Tue,Thu", 1050, 1140, "Lab 6"),
            ("MT-202", "Linear Algebra", "Dr. Farah Siddiqui", 3, 40, "Tue,Thu", 480, 540, "Room 2"),
            ("HU-102", "Professional Ethics", "Ms. Sadia Rehman", 2, 40, "Fri", 480, 540, "Room 4"),
            ("CS-314", "Compiler Construction", "Dr. Asma Javed", 3, 30, "Mon,Wed", 1050, 1140, "Room 10")]
        c.executemany("INSERT INTO courses(code,title,instructor,credits,capacity,days,start,end,room) VALUES(?,?,?,?,?,?,?,?,?)", courses)
        c.executemany("INSERT INTO enrollments VALUES(?,?)", [(1, 1), (1, 2), (1, 3), (2, 6)])
        t = datetime.date.today()
        d = lambda n: str(t + datetime.timedelta(days=n))
        c.executemany("INSERT INTO deadlines(course_id,title,due) VALUES(?,?,?)", [
            (1, "HCI Lab 6 submission", d(1)), (2, "Database assignment 3", d(3)), (3, "OS quiz 2", d(7)),
            (4, "SE project proposal", d(5)), (5, "Networks lab report", d(2)), (7, "Statistics quiz", d(10)), (9, "Report writing task", d(6))])
        c.executemany("INSERT INTO notices(title,created) VALUES(?,?)", [
            ("Course registration closes this week", d(-3)), ("Library timings change on Friday", d(-2)),
            ("Midterm datesheet is now available", d(-1)),
            ("New elective courses added for this semester", d(-1)), ("Fee challan due date extended", d(0))])
        c.commit()
    c.close()

def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(_):
    d = g.pop("db", None)
    if d:
        d.close()

def need_login(f):
    @wraps(f)
    def w(*a, **k):
        if "uid" not in session:
            return jsonify(error="Please sign in."), 401
        return f(*a, **k)
    return w

def course_rows(uid):
    rows = db().execute("""SELECT c.*,
      (SELECT COUNT(*) FROM enrollments e WHERE e.course_id=c.id) AS taken,
      EXISTS(SELECT 1 FROM enrollments e WHERE e.course_id=c.id AND e.student_id=?) AS enrolled,
      EXISTS(SELECT 1 FROM waitlist w WHERE w.course_id=c.id AND w.student_id=?) AS waitlisted
      FROM courses c ORDER BY c.code""", (uid, uid)).fetchall()
    return [dict(r) for r in rows]

@app.get("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.post("/api/login")
def login():
    d = request.get_json(silent=True) or {}
    s = db().execute("SELECT * FROM students WHERE sid=?", (str(d.get("sid", "")).strip().upper(),)).fetchone()
    if not s or not check_password_hash(s["password_hash"], str(d.get("password", ""))):
        return jsonify(error="Wrong student ID or password. Check both and try again."), 401
    session["uid"] = s["id"]
    return jsonify(ok=True)

@app.post("/api/logout")
def logout():
    session.clear()
    return jsonify(ok=True)

@app.get("/api/me")
@need_login
def me():
    s = db().execute("SELECT sid,name,program,semester FROM students WHERE id=?", (session["uid"],)).fetchone()
    return jsonify(dict(s))

@app.get("/api/courses")
@need_login
def courses():
    return jsonify(courses=course_rows(session["uid"]))

@app.get("/api/dashboard")
@need_login
def dashboard():
    uid = session["uid"]
    rows = course_rows(uid)
    mine = [c for c in rows if c["enrolled"]]
    day = datetime.date.today().strftime("%a")
    today = sorted([c for c in mine if day in c["days"].split(",")], key=lambda c: c["start"])
    dl = db().execute("""SELECT d.title, d.due, c.code FROM deadlines d JOIN enrollments e ON e.course_id=d.course_id AND e.student_id=?
      JOIN courses c ON c.id=d.course_id WHERE d.due>=? ORDER BY d.due LIMIT 5""", (uid, str(datetime.date.today()))).fetchall()
    nt = db().execute("SELECT title, created FROM notices ORDER BY id DESC LIMIT 3").fetchall()
    return jsonify(courses=mine, today=today, day=day, deadlines=[dict(r) for r in dl], notices=[dict(r) for r in nt],
                   credits=sum(c["credits"] for c in mine), max_credits=MAX_CREDITS,
                   waitlisted=sum(1 for c in rows if c["waitlisted"]))

@app.post("/api/register")
@need_login
def register():
    uid = session["uid"]
    cid = (request.get_json(silent=True) or {}).get("course_id")
    rows = {c["id"]: c for c in course_rows(uid)}
    c = rows.get(cid)
    if not c:
        return jsonify(error="That course does not exist.", code="INVALID"), 400
    if c["enrolled"]:
        return jsonify(error="You are already registered for this course.", code="DUP"), 409
    if c["taken"] >= c["capacity"]:
        return jsonify(error=c["code"] + " is full.", code="FULL"), 409
    mine = [x for x in rows.values() if x["enrolled"]]
    if sum(x["credits"] for x in mine) + c["credits"] > MAX_CREDITS:
        return jsonify(error="This would pass the limit of %d credit hours." % MAX_CREDITS, code="LIMIT"), 409
    for x in mine:
        if set(x["days"].split(",")) & set(c["days"].split(",")) and x["start"] < c["end"] and c["start"] < x["end"]:
            return jsonify(error="Time clash with %s %s." % (x["code"], x["title"]), code="CLASH"), 409
    db().execute("INSERT INTO enrollments VALUES(?,?)", (uid, cid))
    db().execute("DELETE FROM waitlist WHERE student_id=? AND course_id=?", (uid, cid))
    db().commit()
    return jsonify(ok=True, message="Registered for %s." % c["code"])

@app.post("/api/waitlist")
@need_login
def join_waitlist():
    uid = session["uid"]
    cid = (request.get_json(silent=True) or {}).get("course_id")
    c = {x["id"]: x for x in course_rows(uid)}.get(cid)
    if not c or c["enrolled"]:
        return jsonify(error="You cannot join this waitlist.", code="INVALID"), 400
    db().execute("INSERT OR IGNORE INTO waitlist VALUES(?,?)", (uid, cid))
    db().commit()
    return jsonify(ok=True, message="Added to the waitlist for %s." % c["code"])

@app.delete("/api/register/<int:cid>")
@need_login
def drop(cid):
    db().execute("DELETE FROM enrollments WHERE student_id=? AND course_id=?", (session["uid"], cid))
    db().commit()
    return jsonify(ok=True, message="Course dropped.")

@app.get("/api/notices")
@need_login
def notices():
    return jsonify(notices=[dict(r) for r in db().execute("SELECT title, created FROM notices ORDER BY id DESC")])

@app.post("/api/feedback")
@need_login
def feedback():
    a = (request.get_json(silent=True) or {}).get("answers")
    ok = (isinstance(a, list) and len(a) == 5 and all(isinstance(a[i], int) and 1 <= a[i] <= 5 for i in (0, 1, 3))
          and a[2] in ("Very easily", "With some effort", "Not easily") and isinstance(a[4], str) and len(a[4]) <= 500)
    if not ok:
        return jsonify(error="Please answer questions 1 to 4."), 400
    db().execute("INSERT INTO feedback(student_id,answers,created) VALUES(?,?,?)", (session["uid"], json.dumps(a), str(datetime.date.today())))
    db().commit()
    return jsonify(ok=True)

init_db()

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
