
import sys

KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef", "union", "unsigned", "void",
    "volatile", "while",
}

MULTI_CHAR_OPERATORS = [
    "<<=", ">>=",
    "==", "!=", "<=", ">=", "&&", "||", "++", "--",
    "+=", "-=", "*=", "/=", "%=", "->", "<<", ">>",
    "&=", "|=", "^=",
]

SINGLE_CHAR_OPERATORS = set("+-*/%=<>!&|^")

PUNCTUATION = set("(){}[];,.:")

class Token:
    def __init__(self, ttype, lexeme, line):
        self.ttype = ttype
        self.lexeme = lexeme
        self.line = line


class LexError:
    def __init__(self, message, line):
        self.message = message
        self.line = line

class Lexer:
    def __init__(self, source: str):
        self.src = source
        self.n = len(source)
        self.pos = 0
        self.line = 1
        self.tokens = []
        self.errors = []

    def peek(self, offset=0):
        p = self.pos + offset
        if p < self.n:
            return self.src[p]
        return ""

    def advance(self):
        ch = self.src[self.pos]
        self.pos += 1
        if ch == "\n":
            self.line += 1
        return ch

    def skip_rest_of_line(self):
        """Discard everything up to (but not including) the next
        newline, so line counting stays correct and no further tokens
        are generated for the offending line."""
        while self.pos < self.n and self.src[self.pos] != "\n":
            self.pos += 1

    def tokenize(self):
        while self.pos < self.n:
            ch = self.peek()

            # whitespace
            if ch in (" ", "\t", "\r"):
                self.advance()
                continue

            if ch == "\n":
                self.advance()
                continue

            # comments /* ... */
            if ch == "/" and self.peek(1) == "*":
                self.read_comment()
                continue

            # identifiers / keywords
            if ch.isalpha() or ch == "_":
                self.read_identifier()
                continue

            # integer constants
            if ch.isdigit():
                self.read_number()
                continue

            # string constants
            if ch == '"':
                self.read_string()
                continue

            # char constants
            if ch == "'":
                self.read_char()
                continue

            # multi-character operators (checked before single-char ones)
            matched = False
            for op in MULTI_CHAR_OPERATORS:
                if self.src.startswith(op, self.pos):
                    line = self.line
                    for _ in op:
                        self.advance()
                    self.tokens.append(Token("OPERATOR", op, line))
                    matched = True
                    break
            if matched:
                continue

            # single-character operators
            if ch in SINGLE_CHAR_OPERATORS:
                line = self.line
                self.advance()
                self.tokens.append(Token("OPERATOR", ch, line))
                continue

            # punctuation
            if ch in PUNCTUATION:
                line = self.line
                self.advance()
                self.tokens.append(Token("PUNCTUATION", ch, line))
                continue

            # anything else (e.g. '~', '#', '@', '$') -> undefined symbol
            line = self.line
            bad = self.advance()
            self.errors.append(LexError(f"Undefined symbol '{bad}'", line))
            self.skip_rest_of_line()

        return self.tokens, self.errors

    def read_comment(self):
        start_line = self.line
        self.advance()  # '/'
        self.advance()  # '*'
        closed = False
        while self.pos < self.n:
            if self.peek() == "*" and self.peek(1) == "/":
                self.advance()
                self.advance()
                closed = True
                break
            self.advance()
        if not closed:
            self.errors.append(LexError("Unterminated comment", start_line))
            # We don't know where the comment was meant to end, so nothing
            # after it can be safely tokenized -> stop scanning entirely.
            self.pos = self.n

    def read_identifier(self):
        line = self.line
        start = self.pos
        while self.pos < self.n and (self.peek().isalnum() or self.peek() == "_"):
            self.advance()
        lexeme = self.src[start:self.pos]
        if lexeme in KEYWORDS:
            self.tokens.append(Token("KEYWORD", lexeme, line))
        else:
            self.tokens.append(Token("IDENTIFIER", lexeme, line))

    def read_number(self):
        line = self.line
        start = self.pos
        while self.pos < self.n and self.peek().isdigit():
            self.advance()

        # A digit sequence immediately followed by a letter/underscore is
        # neither a valid number nor a valid identifier (identifiers must
        # start with a letter) -> undefined symbol.
        if self.pos < self.n and (self.peek().isalpha() or self.peek() == "_"):
            while self.pos < self.n and (self.peek().isalnum() or self.peek() == "_"):
                self.advance()
            lexeme = self.src[start:self.pos]
            self.errors.append(LexError(f"Undefined symbol '{lexeme}'", line))
            self.skip_rest_of_line()
            return

        lexeme = self.src[start:self.pos]
        self.tokens.append(Token("INTEGER_CONSTANT", lexeme, line))

    def read_string(self):
        line = self.line
        start = self.pos
        self.advance()  # opening quote
        while True:
            if self.pos >= self.n or self.peek() == "\n":
                self.errors.append(LexError("String constant exceeds line", line))
                self.skip_rest_of_line()
                return
            if self.peek() == '"':
                self.advance()
                break
            self.advance()
        lexeme = self.src[start:self.pos]
        self.tokens.append(Token("STRING_CONSTANT", lexeme, line))

    def read_char(self):
        line = self.line
        start = self.pos
        self.advance()  # opening quote
        if self.pos >= self.n or self.peek() == "\n":
            self.errors.append(LexError("Char constant too long", line))
            self.skip_rest_of_line()
            return

        self.advance()  # the single character inside
        if self.pos < self.n and self.peek() == "'":
            self.advance()
            lexeme = self.src[start:self.pos]
            self.tokens.append(Token("CHAR_CONSTANT", lexeme, line))
        else:
            # more than one char before the closing quote, or missing quote
            self.errors.append(LexError("Char constant too long", line))
            self.skip_rest_of_line()


# --------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------

def run(input_path: str, output_path: str):
    with open(input_path, "r") as f:
        source = f.read()

    lexer = Lexer(source)
    tokens, errors = lexer.tokenize()

    events = [("TOKEN", t.line, t) for t in tokens] + \
             [("ERROR", e.line, e) for e in errors]
    events.sort(key=lambda x: x[1])

    with open(output_path, "w") as out:
        for kind, line, obj in events:
            if kind == "TOKEN":
                out.write(f"Token   : {obj.ttype}\n")
                out.write(f"Lexeme  : {obj.lexeme}\n")
                out.write(f"Line No : {obj.line}\n")
                out.write("-" * 30 + "\n")
            else:
                out.write(f"ERROR   : {obj.message}\n")
                out.write(f"Line No : {obj.line}\n")
                out.write("-" * 30 + "\n")

    print(f"Done. {len(tokens)} tokens, {len(errors)} errors written to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        run(sys.argv[1], sys.argv[2])
    else:
        run("input_source.c", "output_tokens.txt")