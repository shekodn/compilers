#!/usr/bin/python3

from lexer.lexer import lexer, tokens


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

parser = yacc.yacc()
