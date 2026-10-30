# CampusLink LMS (prototype)

Covers HCI Lab 5 (course registration flow) and Lab 6 (student dashboard + feedback).

## Stack
- Frontend: HTML, CSS, vanilla JS single page app (`static/index.html`)
- Backend: Python Flask REST API (`app.py`)
- Database: SQLite file `lms.db`, created and filled with demo data on first run

## Run locally
1. Install Python 3.10+ from python.org (tick "Add to PATH").
2. Open a terminal in this folder.
3. (Optional) `python -m venv venv` then `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux).
4. `pip install -r requirements.txt`
5. `python app.py`
6. Open http://localhost:5000
7. Sign in with `24F-CS-001` / `student123` (second account: `24F-CS-002`).
To reset the data, stop the server and delete `lms.db`.

## Database tables
students, courses, enrollments, waitlist, deadlines, notices, feedback (see `SCHEMA` in `app.py`).

## API (all JSON, session cookie login)
POST /api/login, POST /api/logout, GET /api/me, GET /api/dashboard, GET /api/courses,
POST /api/register {course_id}, POST /api/waitlist {course_id}, DELETE /api/register/<id>,
GET /api/notices, POST /api/feedback {answers:[q1,q2,q3,q4,q5]}.
18 demo courses. Registration checks: already enrolled, course full (offers waitlist), 18 credit limit, time clash.

## Deploy later (Render, free tier)
1. Push this folder to GitHub.
2. Render > New > Web Service > pick the repo.
3. Build command: `pip install -r requirements.txt`; Start command: `gunicorn app:app`.
4. Add env var `SECRET_KEY` (any long random text).
5. Free Render disks reset, so the SQLite data resets on redeploy. For real use, switch to PostgreSQL (Render or Supabase) or attach a persistent disk and set `DB_PATH`.
Alternative: PythonAnywhere free plan works with Flask and keeps SQLite files.

## Prototype limits
Demo data only, no admin panel, no password reset, no grades or assignments.
