#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Reference: https://www.dabeaz.com/ply/ply.html#ply_nn24
#
# -----------------------------------------------------------------------------

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
# t_program = r'[a-zA-Z_][a-zA-Z0-9_]*'#
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

lex.lex()

# def p_BLOQUE(p):
#     "BLOQUE : '{' expression '}'"
#     p[0] = p[2]

start = "PROGRAM"


def p_PROGRAM(p):
    """
    PROGRAM : program id sc PROGRAM_A
    """
    # BLOQUE
    print("status 200")


def p_PROGRAM_A(p):
    """
    PROGRAM_A : VARS
            | EMPTY
    """


def p_VARS(p):
    "VARS : var VARS_A"


def p_VARS_A(p):
    """
    VARS_A : id comma VARS_A
            | id colon TYPE sc p_VARS_B
    """


def p_VARS_B(p):
    """
    p_VARS_B : VARS_A
             | EMPTY
    """


def p_TYPE(p):
    """
    TYPE : float
         | int
    """


def p_BLOQUE(p):
    """
    BLOQUE : lb BLOQUE_A rb
    """


def p_BLOQUE_A(p):
    """
    BLOQUE_A : ESTATUTO BLOQUE_A
             | EMPTY
    """


def p_ESTATUTO(p):
    """
    ESTATUTO : ASIGNACION
             | CONDICION
             | ESCRITURA
    """


def p_ASIGNACION(p):
    """
    ASIGNACION : id eq EXPRESION sc
    """


def p_ESCRITURA(p):
    """
    ESCRITURA : print lp ESCRITURA_A rp sc
    """


def p_ESCRITURA_A(p):
    """
    ESCRITURA_A : ESCRITURA_B comma ESCRITURA_A
                | ESCRITURA_B
    """


def p_ESCRITURA_B(p):
    """
    ESCRITURA_B : string
                | EXPRESION
    """


def p_EXPRESION(p):
    """
    EXPRESION : EXP EXPRESION_A
    """


def p_EXPRESION_A(p):
    """
    EXPRESION_A : rel EXP
                | EMPTY
    """


def p_CONDICION(p):
    """
    CONDICION : if lp EXPRESION rp BLOQUE CONDICION_A sc
    """


def p_CONDICION_A(p):
    """
    CONDICION_A : else BLOQUE
                | EMPTY
    """


def p_EXP(p):
    """
    EXP : TERMINO sign EXP
        | TERMINO
    """


def p_TERMINO(p):
    """
    TERMINO : FACTOR lp TERMINO
            | FACTOR
    """


def p_FACTOR(p):
    """
    FACTOR : lp EXPRESION rp
           | FACTOR_A VARCTE
    """


def p_FACTOR_A(p):
    """
    FACTOR_A : sign
             | EMPTY
    """


def p_VARCTE(p):
    """
    VARCTE : id
           | cteInt
           | cteFloat
    """


# Empty Production
def p_EMPTY(p):
    "EMPTY :"
    pass


def p_error(p):
    print("Syntax error at '%s'" % p.value)


import ply.yacc as yacc

yacc.yacc()

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, "r")
            data = f.read()
            f.close()
            yacc.parse(data, tracking=True)
        except EOFError:
            print("EOFError")
    else:
        print("File missing")
