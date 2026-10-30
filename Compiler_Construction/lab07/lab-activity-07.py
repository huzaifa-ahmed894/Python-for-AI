# Lab-Activity-07
# Dear Students,
#     You are required to implement a Predictive Parser for the following grammar:
#      Type --> Simple | Complex
#      Simple --> int | float | char
#      Complex--> array[num] ofType | struct of Type
      
#     Parse a string using the grammar and display if the syntax is correct or not.
# tokens = []


pos = 0


def look():
    # current word, or "end" if no words are left
    if pos < len(tokens):
        return tokens[pos]
    return "end"


def match(word):
    # if current word is what we expect, move ahead and return True
    global pos
    if look() == word:
        pos = pos + 1
        return True
    return False


def match_num():
    global pos
    if look().isdigit():
        pos = pos + 1
        return True
    return False


def Type():
    if look() in ["int", "float", "char"]:
        return Simple()
    elif look() in ["array", "struct"]:
        return Complex()
    else:
        return False


def Simple():
    return match(look())


def Complex():
    if look() == "array":
        return match("array") and match("[") and match_num() and match("]") and match("of") and Type()
    else:
        return match("struct") and match("of") and Type()


def check(text):
    global tokens, pos
    # put spaces around brackets so split() works
    text = text.replace("[", " [ ").replace("]", " ] ")
    tokens = text.split()
    pos = 0

    # correct only if Type() worked AND no extra words are left
    if Type() and look() == "end":
        print("Syntax is CORRECT")
    else:
        print("Syntax is INCORRECT")


while True:
    s = input("\nEnter string (or quit): ")
    if s == "quit":
        break
    check(s)