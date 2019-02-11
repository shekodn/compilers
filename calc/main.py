#!/usr/bin/python3
# -----------------------------------------------------------------------------
# https://www.dabeaz.com/ply/ply.html#ply_nn24
#
# -----------------------------------------------------------------------------

reserved = {
    'var' : 'var',
    'int' : 'int',
    'float' : 'float',
    'if' : 'if',
    'else' : 'else',
    'print' : 'print',
}


tokens = [
    "program",
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
] + list(reserved.values())


# Tokens
t_program = r'[a-zA-Z_][a-zA-Z0-9_]*'#
t_sc = r'\;'
t_comma = r'\,'
t_colon = r'\:'
t_eq = r'='#
t_notequal = r'<>'
t_gt = r'<'
t_lt = r'>'
t_lp = r'\('#
t_rp = r'\)'#
t_plus = r'\+' #
t_minus = r'-' #
t_times = r'\*'#
t_divide = r'/'#

literals = [ '{', '}' ]

def t_cteFloat(t):
	r'[0-9]+\.[0-9]+'
	t.value = float(t.value)
	return t

def t_cteInt(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t

def t_cteString(t):
	r'\".*\"'
	t.value = str(t.value)
	return t

def t_id(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in reserved:
		t.type = reserved[t.value]
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
    r'\#.*'
    pass
    # No return value. Token discarded

def t_LB(t):
    r'\{'
    t.type = '{'      # Set token type to the expected literal
    return t

def t_RB(t):
    r'\}'
    t.type = '}'      # Set token type to the expected literal
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lex.lex()

# Precedence rules for the arithmetic operators
# precedence = (
#     ("left", "PLUS", "MINUS"),
#     ("left", "TIMES", "DIVIDE"),
#     ("right", "UMINUS"),
# )

# dictionary of names (for storing variables)
# names = {}

# def p_statement_program(p):
#     "expression : PROGRAM ID SC A BLOQUE
#                 | VARS
#                 |

# def p_expression_comment(p):
#     "expression : COMMENT"
#     p[0] = p[1]
#     print("COMMENT")

def p_PORGRAM(p):
    '''
    PORGRAM : program id sc PROGRAM_A BLOQUE

    '''

def p_PROGRAM_A(p):
    '''
    PROGRAM_A : VARS
            | empty
    '''

def p_VARS(p):
    "VARS : var VARS_A"

def p_VARS_A(p):
    "VARS_A : var VARS_A"

# def p_digit(p):
#     "digit : digit"
#     p[0] = p[1]

def p_ESTATUTO(p):
    '''
    ESTATUTO : ASIGNACION
             | CONDICION
             | ESCRITURA
    '''
def p_BLOQUE(p):
    "BLOQUE : '{' expression '}'"
    p[0] = p[2]

def p_FACTOR(p):
    """
    FACTOR : lp EXP rp
           | FACTOR_A VARCTE
           | FACTOR_B
    """
def p_FACTOR_A(p):
    """
    FACTOR_A : FACTOR_B VARCTE
    """

def p_FACTOR_B(p):
    """
    FACTOR_B : SIGN
             | empty
    """
    

def p_VARCTE(p):
    """
    VARCTE : id
           | cteInt
           | cteFloat
    """

# Empty Production
def p_empty(p):
    'empty :'
    pass


# def p_CUERPO(p):
#     '''
#     CUERPO : left_cb CUERPO_AUX right_cb
#     '''
#
#
# def p_expression_tipo(p):
#     "expression : INT expression"
#     p[0] = p[1]





#
# def p_expression_vars:
#     "expression : var "
# #
# # def p_expression_uminus(p):
# #     "expression_uminus : MINUS expression %prec UMINUS"
# #     p[0] = -p[2]
#



# def p_type(p):
# 	'''type : INT
# 			   | FLOAT'''

# def p_tipo(p):
#     """tipo: INT
#    | FLOAT"""


# def p_statement_assign(p):
#     "statement : PROGRAM EQ expression"
#     names[p[1]] = p[3]
#
# def p_statement_expr(p):
#     "statement : expression"
#     print(p[1])
#
#
# def p_expression_binop(p):
#     """expression : expression PLUS expression
#                   | expression MINUS expression
#                   | expression TIMES expression
#                   | expression DIVIDE expression"""
#     if p[2] == "+":
#         p[0] = p[1] + p[3]
#     elif p[2] == "-":
#         p[0] = p[1] - p[3]
#     elif p[2] == "*":
#         p[0] = p[1] * p[3]
#     elif p[2] == "/":
#         p[0] = p[1] / p[3]
#
#
# def p_expression_uminus(p):
#     "expression : MINUS expression %prec UMINUS"
#     p[0] = -p[2]
#
#
# def p_expression_group(p):
#     "expression : LP expression RP"
#     p[0] = p[2]
#
#
# def p_expression_number(p):
#     "expression : DIGIT"
#     p[0] = p[1]
#
#
# def p_expression_name(p):
#     "expression : PROGRAM"
#     try:
#         p[0] = names[p[1]]
#     except LookupError:
#         print("Undefined name '%s'" % p[1])
#         p[0] = 0


def p_error(p):
    print("Syntax error at '%s'" % p.value)


import ply.yacc as yacc

yacc.yacc()

while True:
    try:
        s = input("input > ")  # use input() on Python 3
    except EOFError:
        break
    yacc.parse(s)
