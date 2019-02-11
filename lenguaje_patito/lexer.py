#!/usr/bin/python3

reserved = {
    "var": "var",
    "int": "int",
    "float": "float",
    "if": "if",
    "else": "else",
    "print": "print",
    "program": "program",
}

tokens = [
    "id",
    "sc",
    "comma",
    "colon",
    "digit",
    "lb",
    "rb",
    "eq",
    "gt",
    "lt",
    "notequal",
    "lp",
    "rp",
    "plus",
    "minus",
    "times",
    "divide",
    "cteInt",
    "cteFloat",
    "cteString",
    "comment",
    "sign",
    "rel",
    "string",
] + list(reserved.values())


# Tokens
t_sc = r"\;"
t_comma = r"\,"
t_colon = r"\:"
t_eq = r"="  #
t_rel = r"<>|>|<"
t_notequal = r"<>"
t_gt = r"<"
t_lt = r">"
t_lp = r"\("  #
t_rp = r"\)"  #
t_plus = r"\+"  #
t_minus = r"-"  #
t_times = r"\*"  #
t_divide = r"/"  #
t_string = r"\"[^\"]*\""

literals = ["{", "}"]


def t_cteFloat(t):
    r"[0-9]+\.[0-9]+"
    t.value = float(t.value)
    return t


def t_cteInt(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t


def t_cteString(t):
    r"\".*\""
    t.value = str(t.value)
    return t


def t_id(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_sign(t):
    r"\+|-"
    return t


def t_DIGIT(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_COMMENT(t):
    r"\#.*"
    pass
    # No return value. Token discarded


def t_LB(t):
    r"\{"
    t.type = "{"  # Set token type to the expected literal
    return t


def t_RB(t):
    r"\}"
    t.type = "}"  # Set token type to the expected literal
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()
