keywords = ["int", "float", "char", "if", "else", "while", "for", "return", "void"]

code = open("input.c").read()
out = open("output.txt", "w")
out.write("Token\tLexeme\tLine No\n")

def add(token, lexeme, line):
    out.write(token + "\t" + lexeme + "\t" + str(line) + "\n")

i = 0
line = 1
n = len(code)
error = ""

while i < n:
    ch = code[i]

    if ch == "\n":
        line += 1
        i += 1

    elif ch.isspace():
        i += 1

    # comment /* ... */
    elif ch == "/" and i + 1 < n and code[i + 1] == "*":
        start = line
        i += 2
        while i < n and not (code[i] == "*" and i + 1 < n and code[i + 1] == "/"):
            if code[i] == "\n":
                line += 1
            i += 1
        if i >= n:
            add("ERROR", "Un-terminated comment", start)
        else:
            i += 2

    # identifier or keyword (can now start with @)
    elif ch.isalpha() or ch == "@":
        word = ch
        i += 1
        while i < n and (code[i].isalnum() or code[i] == "_"):
            word += code[i]
            i += 1
        if word in keywords:
            add("KEYWORD", word, line)
        else:
            add("ID", word, line)

    # unsigned integer
    elif ch.isdigit():
        num = ""
        while i < n and code[i].isdigit():
            num += code[i]
            i += 1
        add("NUMBER", num, line)

    # string "..."
    elif ch == '"':
        s = '"'
        i += 1
        while i < n and code[i] != '"' and code[i] != "\n":
            s += code[i]
            i += 1
        if i < n and code[i] == '"':
            add("STRING", s + '"', line)
            i += 1
        else:
            error = "String constant exceeds line"

    # char '...'
    elif ch == "'":
        s = ""
        i += 1
        while i < n and code[i] != "'" and code[i] != "\n":
            s += code[i]
            i += 1
        if i < n and code[i] == "'" and len(s) == 1:
            add("CHAR", "'" + s + "'", line)
            i += 1
        else:
            error = "Char constant too long"

    # operators
    elif ch in "=!<>":
        if i + 1 < n and code[i + 1] == "=":
            add("OPERATOR", ch + "=", line)
            i += 2
        else:
            add("OPERATOR", ch, line)
            i += 1

    elif ch in "+-*/%&|":
        add("OPERATOR", ch, line)
        i += 1

    elif ch in "(){}[];,":
        add("PUNCTUATION", ch, line)
        i += 1

    # anything else (~ # etc.)
    else:
        error = "Undefined symbol " + ch

    # on error: report it and skip the rest of the line
    if error != "":
        add("ERROR", error, line)
        while i < n and code[i] != "\n":
            i += 1
        error = ""

out.close()