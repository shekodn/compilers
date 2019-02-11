
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMcolon comma comment cteFloat cteInt cteString digit divide else eq float gt id if int lb lp lt minus notequal plus print program rb rel rp sc sign string times var\n    PROGRAM : program id sc PROGRAM_A\n    \n    PROGRAM_A : VARS\n            | EMPTY\n    VARS : var VARS_A\n    VARS_A : id comma VARS_A\n            | id colon TYPE sc p_VARS_B\n    \n    p_VARS_B : VARS_A\n             | EMPTY\n    \n    TYPE : float\n         | int\n    \n    BLOQUE : lb BLOQUE_A rb\n    \n    BLOQUE_A : ESTATUTO BLOQUE_A\n             | EMPTY\n    \n    ESTATUTO : ASIGNACION\n             | CONDICION\n             | ESCRITURA\n    \n    ASIGNACION : id eq EXPRESION sc\n    \n    ESCRITURA : print lp ESCRITURA_A rp sc\n    \n    ESCRITURA_A : ESCRITURA_B comma ESCRITURA_A\n                | ESCRITURA_B\n    \n    ESCRITURA_B : string\n                | EXPRESION\n    \n    EXPRESION : EXP EXPRESION_A\n    \n    EXPRESION_A : rel EXP\n                | EMPTY\n    \n    CONDICION : if lp EXPRESION rp BLOQUE CONDICION_A sc\n    \n    CONDICION_A : else BLOQUE\n                | EMPTY\n    \n    EXP : TERMINO sign EXP\n        | TERMINO\n    \n    TERMINO : FACTOR lp TERMINO\n            | FACTOR\n    \n    FACTOR : lp EXPRESION rp\n           | FACTOR_A VARCTE\n    \n    FACTOR_A : sign\n             | EMPTY\n    \n    VARCTE : id\n           | cteInt\n           | cteFloat\n    EMPTY :'
    
_lr_action_items = {'int':([12,],[14,]),'float':([12,],[15,]),'var':([4,],[7,]),'program':([0,],[1,]),'colon':([10,],[12,]),'sc':([3,14,15,16,],[4,-10,-9,17,]),'comma':([10,],[11,]),'id':([1,7,11,17,],[3,10,10,10,]),'$end':([2,4,5,6,8,9,13,17,18,19,20,],[0,-40,-1,-2,-3,-4,-5,-40,-6,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM_A':([4,],[5,]),'VARS':([4,],[6,]),'p_VARS_B':([17,],[18,]),'VARS_A':([7,11,17,],[9,13,19,]),'PROGRAM':([0,],[2,]),'TYPE':([12,],[16,]),'EMPTY':([4,17,],[8,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> program id sc PROGRAM_A','PROGRAM',4,'p_PROGRAM','parser.py',11),
  ('PROGRAM_A -> VARS','PROGRAM_A',1,'p_PROGRAM_A','parser.py',19),
  ('PROGRAM_A -> EMPTY','PROGRAM_A',1,'p_PROGRAM_A','parser.py',20),
  ('VARS -> var VARS_A','VARS',2,'p_VARS','parser.py',25),
  ('VARS_A -> id comma VARS_A','VARS_A',3,'p_VARS_A','parser.py',30),
  ('VARS_A -> id colon TYPE sc p_VARS_B','VARS_A',5,'p_VARS_A','parser.py',31),
  ('p_VARS_B -> VARS_A','p_VARS_B',1,'p_VARS_B','parser.py',37),
  ('p_VARS_B -> EMPTY','p_VARS_B',1,'p_VARS_B','parser.py',38),
  ('TYPE -> float','TYPE',1,'p_TYPE','parser.py',44),
  ('TYPE -> int','TYPE',1,'p_TYPE','parser.py',45),
  ('BLOQUE -> lb BLOQUE_A rb','BLOQUE',3,'p_BLOQUE','parser.py',51),
  ('BLOQUE_A -> ESTATUTO BLOQUE_A','BLOQUE_A',2,'p_BLOQUE_A','parser.py',57),
  ('BLOQUE_A -> EMPTY','BLOQUE_A',1,'p_BLOQUE_A','parser.py',58),
  ('ESTATUTO -> ASIGNACION','ESTATUTO',1,'p_ESTATUTO','parser.py',64),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_ESTATUTO','parser.py',65),
  ('ESTATUTO -> ESCRITURA','ESTATUTO',1,'p_ESTATUTO','parser.py',66),
  ('ASIGNACION -> id eq EXPRESION sc','ASIGNACION',4,'p_ASIGNACION','parser.py',72),
  ('ESCRITURA -> print lp ESCRITURA_A rp sc','ESCRITURA',5,'p_ESCRITURA','parser.py',78),
  ('ESCRITURA_A -> ESCRITURA_B comma ESCRITURA_A','ESCRITURA_A',3,'p_ESCRITURA_A','parser.py',84),
  ('ESCRITURA_A -> ESCRITURA_B','ESCRITURA_A',1,'p_ESCRITURA_A','parser.py',85),
  ('ESCRITURA_B -> string','ESCRITURA_B',1,'p_ESCRITURA_B','parser.py',91),
  ('ESCRITURA_B -> EXPRESION','ESCRITURA_B',1,'p_ESCRITURA_B','parser.py',92),
  ('EXPRESION -> EXP EXPRESION_A','EXPRESION',2,'p_EXPRESION','parser.py',98),
  ('EXPRESION_A -> rel EXP','EXPRESION_A',2,'p_EXPRESION_A','parser.py',104),
  ('EXPRESION_A -> EMPTY','EXPRESION_A',1,'p_EXPRESION_A','parser.py',105),
  ('CONDICION -> if lp EXPRESION rp BLOQUE CONDICION_A sc','CONDICION',7,'p_CONDICION','parser.py',111),
  ('CONDICION_A -> else BLOQUE','CONDICION_A',2,'p_CONDICION_A','parser.py',117),
  ('CONDICION_A -> EMPTY','CONDICION_A',1,'p_CONDICION_A','parser.py',118),
  ('EXP -> TERMINO sign EXP','EXP',3,'p_EXP','parser.py',124),
  ('EXP -> TERMINO','EXP',1,'p_EXP','parser.py',125),
  ('TERMINO -> FACTOR lp TERMINO','TERMINO',3,'p_TERMINO','parser.py',131),
  ('TERMINO -> FACTOR','TERMINO',1,'p_TERMINO','parser.py',132),
  ('FACTOR -> lp EXPRESION rp','FACTOR',3,'p_FACTOR','parser.py',138),
  ('FACTOR -> FACTOR_A VARCTE','FACTOR',2,'p_FACTOR','parser.py',139),
  ('FACTOR_A -> sign','FACTOR_A',1,'p_FACTOR_A','parser.py',145),
  ('FACTOR_A -> EMPTY','FACTOR_A',1,'p_FACTOR_A','parser.py',146),
  ('VARCTE -> id','VARCTE',1,'p_VARCTE','parser.py',152),
  ('VARCTE -> cteInt','VARCTE',1,'p_VARCTE','parser.py',153),
  ('VARCTE -> cteFloat','VARCTE',1,'p_VARCTE','parser.py',154),
  ('EMPTY -> <empty>','EMPTY',0,'p_EMPTY','parser.py',160),
]