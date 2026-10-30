"""
Lexical Analyzer for C (Phase 1) - single script.
Reads  : source.c   (C source code)
Writes : tokens_output.txt  (Token | Lexeme | Line No)
Also prints the result on the screen.
"""

KEYWORDS = {"int", "float", "char", "void", "if", "else",
            "while", "for", "return", "main"}

TWO_CHAR_SYMBOLS = {"==", "!=", "<=", ">=", "&&", "||", "++", "--"}
ONE_CHAR_SYMBOLS = set("+-*/%=<>!&|(){}[];,")


def is_letter(c):
    return c.isalpha()          # case-sensitive: 'A' and 'a' are different


def is_digit(c):
    return c.isdigit()


def tokenize(src):
    """Return a list of result lines (tokens and errors)."""
    out = []
    i = 0                       # current position in the source text
    line = 1                    # current line number
    n = len(src)

    def add(token, lexeme, ln):
        out.append(f"{token:<14}| {lexeme:<24}| {ln}")

    def error(message, ln):
        out.append(f"{'ERROR':<14}| {message:<24}| {ln}")

    def skip_rest_of_line(pos):
        """Move pos to the '\\n' that ends the current line (or end of file)."""
        while pos < n and src[pos] != "\n":
            pos += 1
        return pos

    while i < n:
        c = src[i]

        # ---- whitespace ----
        if c == "\n":
            line += 1
            i += 1
            continue
        if c.isspace():
            i += 1
            continue

        # ---- block comment  /* ... */  (no nesting, may span lines) ----
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            start_line = line
            i += 2
            closed = False
            while i < n:
                if src[i] == "*" and i + 1 < n and src[i + 1] == "/":
                    i += 2
                    closed = True
                    break
                if src[i] == "\n":
                    line += 1
                i += 1
            if not closed:
                error("Unterminated comment", start_line)
            continue

        # ---- identifier / keyword : letter (letter | digit | _)* ----
        if is_letter(c):
            start = i
            while i < n and (is_letter(src[i]) or is_digit(src[i]) or src[i] == "_"):
                i += 1
            word = src[start:i]
            add("KEYWORD" if word in KEYWORDS else "IDENTIFIER", word, line)
            continue

        # ---- unsigned integer constant ----
        if is_digit(c):
            start = i
            while i < n and is_digit(src[i]):
                i += 1
            add("INTEGER", src[start:i], line)
            continue

        # ---- string constant "..." (must end on the same line) ----
        if c == '"':
            start = i
            i += 1
            while i < n and src[i] != '"' and src[i] != "\n":
                i += 1
            if i < n and src[i] == '"':
                i += 1
                add("STRING", src[start:i], line)
            else:
                error("String exceeds line", line)
                i = skip_rest_of_line(i)        # error recovery
            continue

        # ---- character constant 'x' (exactly one character) ----
        if c == "'":
            start = i
            i += 1
            while i < n and src[i] != "'" and src[i] != "\n":
                i += 1
            if i < n and src[i] == "'":
                content = src[start + 1:i]
                i += 1
                if len(content) == 1:
                    add("CHAR", src[start:i], line)
                else:
                    error("Char constant too long", line)
                    i = skip_rest_of_line(i)
            else:
                error("Char constant too long", line)
                i = skip_rest_of_line(i)
            continue

        # ---- operators and punctuation ----
        if i + 1 < n and src[i:i + 2] in TWO_CHAR_SYMBOLS:
            add("SYMBOL", src[i:i + 2], line)
            i += 2
            continue
        if c in ONE_CHAR_SYMBOLS:
            add("SYMBOL", c, line)
            i += 1
            continue

        # ---- anything else is an undefined symbol (~ # @ $ _ ...) ----
        error("Undefined symbol", line)
        i = skip_rest_of_line(i)        # ignore the rest of this line

    return out


def main():
    try:
        with open("source.c", "r") as f:
            source = f.read()
    except FileNotFoundError:
        print("Error: 'source.c' not found. Create it and paste your C code in it.")
        return

    header = f"{'TOKEN':<14}| {'LEXEME':<24}| LINE NO"
    lines = [header, "-" * len(header)] + tokenize(source)

    with open("tokens_output.txt", "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()