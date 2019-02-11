# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = "3.10"

_lr_method = "LALR"

_lr_signature = "PROGRAMcolon comma comment cteFloat cteInt cteString digit divide else eq float gt id if int lb lp lt minus notequal plus print program rb rel rp sc sign string times var\n    PROGRAM : program id sc PROGRAM_A\n    \n    PROGRAM_A : VARS\n            | EMPTY\n    VARS : var VARS_A\n    VARS_A : id comma VARS_A\n            | id colon TYPE sc p_VARS_B\n    \n    p_VARS_B : VARS_A\n             | EMPTY\n    \n    TYPE : float\n         | int\n    \n    BLOQUE : lb BLOQUE_A rb\n    \n    BLOQUE_A : ESTATUTO BLOQUE_A\n             | EMPTY\n    \n    ESTATUTO : ASIGNACION\n             | CONDICION\n             | ESCRITURA\n    \n    ASIGNACION : id eq EXPRESION sc\n    \n    ESCRITURA : print lp ESCRITURA_A rp sc\n    \n    ESCRITURA_A : ESCRITURA_B comma ESCRITURA_A\n                | ESCRITURA_B\n    \n    ESCRITURA_B : string\n                | EXPRESION\n    \n    EXPRESION : EXP EXPRESION_A\n    \n    EXPRESION_A : rel EXP\n                | EMPTY\n    \n    CONDICION : if lp EXPRESION rp BLOQUE CONDICION_A sc\n    \n    CONDICION_A : else BLOQUE\n                | EMPTY\n    \n    EXP : TERMINO sign EXP\n        | TERMINO\n    \n    TERMINO : FACTOR lp TERMINO\n            | FACTOR\n    \n    FACTOR : lp EXPRESION rp\n           | FACTOR_A VARCTE\n    \n    FACTOR_A : sign\n             | EMPTY\n    \n    VARCTE : id\n           | cteInt\n           | cteFloat\n    EMPTY :"

_lr_action_items = {
    "program": ([0], [2]),
    "$end": (
        [1, 4, 5, 6, 7, 9, 13, 17, 18, 19, 20],
        [0, -40, -1, -2, -3, -4, -5, -40, -6, -7, -8],
    ),
    "id": ([2, 8, 11, 17], [3, 10, 10, 10]),
    "sc": ([3, 14, 15, 16], [4, 17, -9, -10]),
    "var": ([4], [8]),
    "comma": ([10], [11]),
    "colon": ([10], [12]),
    "float": ([12], [15]),
    "int": ([12], [16]),
}

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:
            _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {
    "PROGRAM": ([0], [1]),
    "PROGRAM_A": ([4], [5]),
    "VARS": ([4], [6]),
    "EMPTY": ([4, 17], [7, 20]),
    "VARS_A": ([8, 11, 17], [9, 13, 19]),
    "TYPE": ([12], [14]),
    "p_VARS_B": ([17], [18]),
}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto:
            _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> PROGRAM", "S'", 1, None, None, None),
    ("PROGRAM -> program id sc PROGRAM_A", "PROGRAM", 4, "p_PROGRAM", "main.py", 136),
    ("PROGRAM_A -> VARS", "PROGRAM_A", 1, "p_PROGRAM_A", "main.py", 143),
    ("PROGRAM_A -> EMPTY", "PROGRAM_A", 1, "p_PROGRAM_A", "main.py", 144),
    ("VARS -> var VARS_A", "VARS", 2, "p_VARS", "main.py", 148),
    ("VARS_A -> id comma VARS_A", "VARS_A", 3, "p_VARS_A", "main.py", 152),
    ("VARS_A -> id colon TYPE sc p_VARS_B", "VARS_A", 5, "p_VARS_A", "main.py", 153),
    ("p_VARS_B -> VARS_A", "p_VARS_B", 1, "p_VARS_B", "main.py", 158),
    ("p_VARS_B -> EMPTY", "p_VARS_B", 1, "p_VARS_B", "main.py", 159),
    ("TYPE -> float", "TYPE", 1, "p_TYPE", "main.py", 164),
    ("TYPE -> int", "TYPE", 1, "p_TYPE", "main.py", 165),
    ("BLOQUE -> lb BLOQUE_A rb", "BLOQUE", 3, "p_BLOQUE", "main.py", 169),
    ("BLOQUE_A -> ESTATUTO BLOQUE_A", "BLOQUE_A", 2, "p_BLOQUE_A", "main.py", 173),
    ("BLOQUE_A -> EMPTY", "BLOQUE_A", 1, "p_BLOQUE_A", "main.py", 174),
    ("ESTATUTO -> ASIGNACION", "ESTATUTO", 1, "p_ESTATUTO", "main.py", 179),
    ("ESTATUTO -> CONDICION", "ESTATUTO", 1, "p_ESTATUTO", "main.py", 180),
    ("ESTATUTO -> ESCRITURA", "ESTATUTO", 1, "p_ESTATUTO", "main.py", 181),
    (
        "ASIGNACION -> id eq EXPRESION sc",
        "ASIGNACION",
        4,
        "p_ASIGNACION",
        "main.py",
        186,
    ),
    (
        "ESCRITURA -> print lp ESCRITURA_A rp sc",
        "ESCRITURA",
        5,
        "p_ESCRITURA",
        "main.py",
        191,
    ),
    (
        "ESCRITURA_A -> ESCRITURA_B comma ESCRITURA_A",
        "ESCRITURA_A",
        3,
        "p_ESCRITURA_A",
        "main.py",
        196,
    ),
    ("ESCRITURA_A -> ESCRITURA_B", "ESCRITURA_A", 1, "p_ESCRITURA_A", "main.py", 197),
    ("ESCRITURA_B -> string", "ESCRITURA_B", 1, "p_ESCRITURA_B", "main.py", 202),
    ("ESCRITURA_B -> EXPRESION", "ESCRITURA_B", 1, "p_ESCRITURA_B", "main.py", 203),
    ("EXPRESION -> EXP EXPRESION_A", "EXPRESION", 2, "p_EXPRESION", "main.py", 208),
    ("EXPRESION_A -> rel EXP", "EXPRESION_A", 2, "p_EXPRESION_A", "main.py", 213),
    ("EXPRESION_A -> EMPTY", "EXPRESION_A", 1, "p_EXPRESION_A", "main.py", 214),
    (
        "CONDICION -> if lp EXPRESION rp BLOQUE CONDICION_A sc",
        "CONDICION",
        7,
        "p_CONDICION",
        "main.py",
        219,
    ),
    ("CONDICION_A -> else BLOQUE", "CONDICION_A", 2, "p_CONDICION_A", "main.py", 223),
    ("CONDICION_A -> EMPTY", "CONDICION_A", 1, "p_CONDICION_A", "main.py", 224),
    ("EXP -> TERMINO sign EXP", "EXP", 3, "p_EXP", "main.py", 229),
    ("EXP -> TERMINO", "EXP", 1, "p_EXP", "main.py", 230),
    ("TERMINO -> FACTOR lp TERMINO", "TERMINO", 3, "p_TERMINO", "main.py", 235),
    ("TERMINO -> FACTOR", "TERMINO", 1, "p_TERMINO", "main.py", 236),
    ("FACTOR -> lp EXPRESION rp", "FACTOR", 3, "p_FACTOR", "main.py", 241),
    ("FACTOR -> FACTOR_A VARCTE", "FACTOR", 2, "p_FACTOR", "main.py", 242),
    ("FACTOR_A -> sign", "FACTOR_A", 1, "p_FACTOR_A", "main.py", 246),
    ("FACTOR_A -> EMPTY", "FACTOR_A", 1, "p_FACTOR_A", "main.py", 247),
    ("VARCTE -> id", "VARCTE", 1, "p_VARCTE", "main.py", 252),
    ("VARCTE -> cteInt", "VARCTE", 1, "p_VARCTE", "main.py", 253),
    ("VARCTE -> cteFloat", "VARCTE", 1, "p_VARCTE", "main.py", 254),
    ("EMPTY -> <empty>", "EMPTY", 0, "p_EMPTY", "main.py", 259),
]
