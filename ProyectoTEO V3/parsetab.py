
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARITMETIC_OP_ADD ARITMETIC_OP_PROD ASSIGN BIT_OP BLOCK_END BLOCK_START CHAR CHARACTER COMA COMILLA_DOBLE DEFINE DO ELSE ESCRITURA FLOAT FOR HASH ID IF INCLUDE INT LECTURA LOGIC_OP LPAREN MINUSMINUS MODIFICADOR NEGATION NUMBER PLUSPLUS PUNTOCOMA RELATION_OP RETURN RPAREN STRING VOID WHILEprogram : include_directives declaration_lempty :include_directives : include_directives include_directive\n                          | include_directive\n                          | empty\n    include_directive : HASH INCLUDE STRING\n                         | HASH DEFINE ID simple_expression \n    declaration_l : declaration_l declaration\n                     | declaration\n    declaration : type var_declaration PUNTOCOMA\n                   | fun_declaration\n    var_declaration : var_declaration COMA var_definition\n                       | var_definition\n    var_definition : ID\n                      | ID ASSIGN simple_expression\n    fun_declaration : type ID LPAREN params RPAREN compound_stmt\n                       | VOID ID LPAREN params RPAREN compound_stmt\n    params : params_l\n              | VOID\n              | empty\n    params_l : params_l COMA param\n                | param\n    param : type IDtype : INT\n            | FLOAT\n            | CHAR\n    expression : ID ASSIGN simple_expression\n                  | simple_expression\n    expression_stmt : expression PUNTOCOMA\n                       | PUNTOCOMA\n    compound_stmt : BLOCK_START local_instructions BLOCK_END\n    local_instructions : local_instructions type var_declaration PUNTOCOMA\n                          | local_instructions statement\n                          | empty\n    statement : expression_stmt \n                 | compound_stmt \n                 | if_stmt \n                 | while_stmt \n                 | do_while_stmt \n                 | return_stmt\n                 | lectura_stm\n                 | escritura_stm\n    return_stmt : RETURN PUNTOCOMA\n                   | RETURN expression PUNTOCOMA\n    if_stmt : IF LPAREN condition RPAREN statement\n               | IF LPAREN condition RPAREN statement ELSE statement\n    while_stmt : WHILE LPAREN condition RPAREN statement\n    do_while_stmt : DO statement \n    condition : NEGATION simple_expression\n                 | condition LOGIC_OP simple_expression\n                 | simple_expression    \n    simple_expression : simple_expression RELATION_OP bit_operation\n                         | bit_operation\n    bit_operation : bit_operation BIT_OP additive_operation\n                     | additive_operation\n    additive_operation : additive_operation ARITMETIC_OP_ADD prod_operation\n                          | prod_operation\n    prod_operation : prod_operation ARITMETIC_OP_PROD factor\n                      | factor\n    factor : LPAREN simple_expression RPAREN\n              | call\n              | ID\n              | NUMBER\n              | CHARACTER   \n     escritura_stm : ESCRITURA LPAREN  STRING  COMA var_multiple RPAREN PUNTOCOMA\n                    | ESCRITURA LPAREN  STRING  RPAREN PUNTOCOMA statement lectura_stm : LECTURA LPAREN COMILLA_DOBLE modificadores COMILLA_DOBLE COMA var_multiple RPAREN PUNTOCOMA statement\n     var_multiple : ID\n                        | ID COMA var_multiple\n     modificadores : MODIFICADOR\n                        | MODIFICADOR modificadores\n    call : ID LPAREN args RPARENargs : args_l\n            | empty\n    args_l : args_l COMA simple_expression\n              | simple_expression \n    '
    
_lr_action_items = {'HASH':([0,2,3,4,7,22,29,30,31,32,33,34,36,37,38,63,64,65,66,67,72,],[5,5,-4,-5,-3,-6,-62,-7,-53,-55,-57,-59,-61,-63,-64,-52,-54,-56,-58,-60,-72,]),'INT':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,57,63,64,65,66,67,68,69,71,72,74,75,77,79,80,81,82,83,84,85,86,87,88,99,102,103,108,113,125,127,137,138,140,144,],[-2,11,-4,-5,11,-3,-9,-11,-8,-6,-10,11,11,-62,-7,-53,-55,-57,-59,-61,-63,-64,11,-52,-54,-56,-58,-60,-16,-2,-17,-72,11,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,-29,-48,-43,-32,-44,-45,-47,-66,-46,-65,-67,]),'FLOAT':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,57,63,64,65,66,67,68,69,71,72,74,75,77,79,80,81,82,83,84,85,86,87,88,99,102,103,108,113,125,127,137,138,140,144,],[-2,12,-4,-5,12,-3,-9,-11,-8,-6,-10,12,12,-62,-7,-53,-55,-57,-59,-61,-63,-64,12,-52,-54,-56,-58,-60,-16,-2,-17,-72,12,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,-29,-48,-43,-32,-44,-45,-47,-66,-46,-65,-67,]),'CHAR':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,57,63,64,65,66,67,68,69,71,72,74,75,77,79,80,81,82,83,84,85,86,87,88,99,102,103,108,113,125,127,137,138,140,144,],[-2,13,-4,-5,13,-3,-9,-11,-8,-6,-10,13,13,-62,-7,-53,-55,-57,-59,-61,-63,-64,13,-52,-54,-56,-58,-60,-16,-2,-17,-72,13,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,-29,-48,-43,-32,-44,-45,-47,-66,-46,-65,-67,]),'VOID':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,63,64,65,66,67,68,71,72,77,],[-2,14,-4,-5,14,-3,-9,-11,-8,-6,-10,44,44,-62,-7,-53,-55,-57,-59,-61,-63,-64,-52,-54,-56,-58,-60,-16,-17,-72,-31,]),'$end':([1,6,8,10,17,24,68,71,77,],[0,-1,-9,-11,-8,-10,-16,-17,-31,]),'INCLUDE':([5,],[15,]),'DEFINE':([5,],[16,]),'ID':([9,11,12,13,14,16,23,25,27,35,41,49,50,51,52,53,69,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,92,93,99,100,101,102,103,107,108,110,113,117,118,120,123,125,127,132,133,134,136,137,138,140,143,144,],[19,-24,-25,-26,21,23,29,40,29,29,55,29,29,29,29,29,-2,29,96,-34,-31,40,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,96,96,-29,29,29,-48,-43,29,-32,29,-44,96,29,96,131,-45,-47,96,96,131,131,-66,-46,-65,96,-67,]),'STRING':([15,106,],[22,115,]),'PUNTOCOMA':([18,19,20,29,31,32,33,34,36,37,38,39,40,47,63,64,65,66,67,69,72,74,75,77,79,80,81,82,83,84,85,86,87,88,89,92,93,96,97,98,99,102,103,104,108,113,116,117,120,124,125,127,132,133,135,137,138,140,142,143,144,],[24,-14,-13,-62,-53,-55,-57,-59,-61,-63,-64,-12,-14,-15,-52,-54,-56,-58,-60,-2,-72,79,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,99,79,103,-62,-28,108,-29,-48,-43,113,-32,-44,-27,79,79,132,-45,-47,79,79,140,-66,-46,-65,143,79,-67,]),'COMA':([18,19,20,29,31,32,33,34,36,37,38,39,40,43,46,47,55,60,62,63,64,65,66,67,70,72,76,98,115,128,131,],[25,-14,-13,-62,-53,-55,-57,-59,-61,-63,-64,-12,-14,57,-22,-15,-23,73,-76,-52,-54,-56,-58,-60,-21,-72,-75,25,123,134,136,]),'LPAREN':([19,21,23,27,29,35,49,50,51,52,53,69,73,74,75,77,79,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96,99,100,101,102,103,107,108,110,113,117,118,120,125,127,132,133,137,138,140,143,144,],[26,28,35,35,49,35,35,35,35,35,35,-2,35,35,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,100,101,35,35,105,106,49,-29,35,35,-48,-43,35,-32,35,-44,35,35,35,-45,-47,35,35,-66,-46,-65,35,-67,]),'ASSIGN':([19,40,96,],[27,27,107,]),'NUMBER':([23,27,35,49,50,51,52,53,69,73,74,75,77,79,80,81,82,83,84,85,86,87,88,92,93,99,100,101,102,103,107,108,110,113,117,118,120,125,127,132,133,137,138,140,143,144,],[37,37,37,37,37,37,37,37,-2,37,37,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,37,37,-29,37,37,-48,-43,37,-32,37,-44,37,37,37,-45,-47,37,37,-66,-46,-65,37,-67,]),'CHARACTER':([23,27,35,49,50,51,52,53,69,73,74,75,77,79,80,81,82,83,84,85,86,87,88,92,93,99,100,101,102,103,107,108,110,113,117,118,120,125,127,132,133,137,138,140,143,144,],[38,38,38,38,38,38,38,38,-2,38,38,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,38,38,-29,38,38,-48,-43,38,-32,38,-44,38,38,38,-45,-47,38,38,-66,-46,-65,38,-67,]),'RPAREN':([26,28,29,31,32,33,34,36,37,38,42,43,44,45,46,48,49,54,55,59,60,61,62,63,64,65,66,67,70,72,76,109,111,112,115,119,126,130,131,139,141,],[-2,-2,-62,-53,-55,-57,-59,-61,-63,-64,56,-18,-19,-20,-22,58,-2,67,-23,72,-73,-74,-76,-52,-54,-56,-58,-60,-21,-72,-75,117,-51,120,124,-49,-50,135,-68,142,-69,]),'ARITMETIC_OP_PROD':([29,33,34,36,37,38,65,66,67,72,96,],[-62,53,-59,-61,-63,-64,53,-58,-60,-72,-62,]),'ARITMETIC_OP_ADD':([29,32,33,34,36,37,38,64,65,66,67,72,96,],[-62,52,-57,-59,-61,-63,-64,52,-56,-58,-60,-72,-62,]),'BIT_OP':([29,31,32,33,34,36,37,38,63,64,65,66,67,72,96,],[-62,51,-55,-57,-59,-61,-63,-64,51,-54,-56,-58,-60,-72,-62,]),'RELATION_OP':([29,30,31,32,33,34,36,37,38,47,54,62,63,64,65,66,67,72,76,96,97,111,116,119,126,],[-62,50,-53,-55,-57,-59,-61,-63,-64,50,50,50,-52,-54,-56,-58,-60,-72,50,-62,50,50,50,50,50,]),'LOGIC_OP':([29,31,32,33,34,36,37,38,63,64,65,66,67,72,109,111,112,119,126,],[-62,-53,-55,-57,-59,-61,-63,-64,-52,-54,-56,-58,-60,-72,118,-51,118,-49,-50,]),'BLOCK_START':([56,58,69,74,75,77,79,80,81,82,83,84,85,86,87,88,92,99,102,103,108,113,117,120,125,127,132,133,137,138,140,143,144,],[69,69,-2,69,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,69,-29,-48,-43,-32,-44,69,69,-45,-47,69,69,-66,-46,-65,69,-67,]),'BLOCK_END':([69,74,75,77,79,80,81,82,83,84,85,86,87,88,99,102,103,108,113,125,127,137,138,140,144,],[-2,77,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,-29,-48,-43,-32,-44,-45,-47,-66,-46,-65,-67,]),'IF':([69,74,75,77,79,80,81,82,83,84,85,86,87,88,92,99,102,103,108,113,117,120,125,127,132,133,137,138,140,143,144,],[-2,90,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,90,-29,-48,-43,-32,-44,90,90,-45,-47,90,90,-66,-46,-65,90,-67,]),'WHILE':([69,74,75,77,79,80,81,82,83,84,85,86,87,88,92,99,102,103,108,113,117,120,125,127,132,133,137,138,140,143,144,],[-2,91,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,91,-29,-48,-43,-32,-44,91,91,-45,-47,91,91,-66,-46,-65,91,-67,]),'DO':([69,74,75,77,79,80,81,82,83,84,85,86,87,88,92,99,102,103,108,113,117,120,125,127,132,133,137,138,140,143,144,],[-2,92,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,92,-29,-48,-43,-32,-44,92,92,-45,-47,92,92,-66,-46,-65,92,-67,]),'RETURN':([69,74,75,77,79,80,81,82,83,84,85,86,87,88,92,99,102,103,108,113,117,120,125,127,132,133,137,138,140,143,144,],[-2,93,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,93,-29,-48,-43,-32,-44,93,93,-45,-47,93,93,-66,-46,-65,93,-67,]),'LECTURA':([69,74,75,77,79,80,81,82,83,84,85,86,87,88,92,99,102,103,108,113,117,120,125,127,132,133,137,138,140,143,144,],[-2,94,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,94,-29,-48,-43,-32,-44,94,94,-45,-47,94,94,-66,-46,-65,94,-67,]),'ESCRITURA':([69,74,75,77,79,80,81,82,83,84,85,86,87,88,92,99,102,103,108,113,117,120,125,127,132,133,137,138,140,143,144,],[-2,95,-34,-31,-30,-33,-35,-36,-37,-38,-39,-40,-41,-42,95,-29,-48,-43,-32,-44,95,95,-45,-47,95,95,-66,-46,-65,95,-67,]),'ELSE':([77,79,81,82,83,84,85,86,87,88,99,102,103,113,125,127,137,138,140,144,],[-31,-30,-35,-36,-37,-38,-39,-40,-41,-42,-29,-48,-43,-44,133,-47,-66,-46,-65,-67,]),'NEGATION':([100,101,],[110,110,]),'COMILLA_DOBLE':([105,121,122,129,],[114,128,-70,-71,]),'MODIFICADOR':([114,122,],[122,122,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'include_directives':([0,],[2,]),'include_directive':([0,2,],[3,7,]),'empty':([0,26,28,49,69,],[4,45,45,61,75,]),'declaration_l':([2,],[6,]),'declaration':([2,6,],[8,17,]),'type':([2,6,26,28,57,74,],[9,9,41,41,41,78,]),'fun_declaration':([2,6,],[10,10,]),'var_declaration':([9,78,],[18,98,]),'var_definition':([9,25,78,],[20,39,20,]),'simple_expression':([23,27,35,49,73,74,92,93,100,101,107,110,117,118,120,132,133,143,],[30,47,54,62,76,97,97,97,111,111,116,119,97,126,97,97,97,97,]),'bit_operation':([23,27,35,49,50,73,74,92,93,100,101,107,110,117,118,120,132,133,143,],[31,31,31,31,63,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'additive_operation':([23,27,35,49,50,51,73,74,92,93,100,101,107,110,117,118,120,132,133,143,],[32,32,32,32,32,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'prod_operation':([23,27,35,49,50,51,52,73,74,92,93,100,101,107,110,117,118,120,132,133,143,],[33,33,33,33,33,33,65,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'factor':([23,27,35,49,50,51,52,53,73,74,92,93,100,101,107,110,117,118,120,132,133,143,],[34,34,34,34,34,34,34,66,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'call':([23,27,35,49,50,51,52,53,73,74,92,93,100,101,107,110,117,118,120,132,133,143,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'params':([26,28,],[42,48,]),'params_l':([26,28,],[43,43,]),'param':([26,28,57,],[46,46,70,]),'args':([49,],[59,]),'args_l':([49,],[60,]),'compound_stmt':([56,58,74,92,117,120,132,133,143,],[68,71,82,82,82,82,82,82,82,]),'local_instructions':([69,],[74,]),'statement':([74,92,117,120,132,133,143,],[80,102,125,127,137,138,144,]),'expression_stmt':([74,92,117,120,132,133,143,],[81,81,81,81,81,81,81,]),'if_stmt':([74,92,117,120,132,133,143,],[83,83,83,83,83,83,83,]),'while_stmt':([74,92,117,120,132,133,143,],[84,84,84,84,84,84,84,]),'do_while_stmt':([74,92,117,120,132,133,143,],[85,85,85,85,85,85,85,]),'return_stmt':([74,92,117,120,132,133,143,],[86,86,86,86,86,86,86,]),'lectura_stm':([74,92,117,120,132,133,143,],[87,87,87,87,87,87,87,]),'escritura_stm':([74,92,117,120,132,133,143,],[88,88,88,88,88,88,88,]),'expression':([74,92,93,117,120,132,133,143,],[89,89,104,89,89,89,89,89,]),'condition':([100,101,],[109,112,]),'modificadores':([114,122,],[121,129,]),'var_multiple':([123,134,136,],[130,139,141,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> include_directives declaration_l','program',2,'p_program','parser_class.py',11),
  ('empty -> <empty>','empty',0,'p_empty','parser_class.py',14),
  ('include_directives -> include_directives include_directive','include_directives',2,'p_include_directives','parser_class.py',20),
  ('include_directives -> include_directive','include_directives',1,'p_include_directives','parser_class.py',21),
  ('include_directives -> empty','include_directives',1,'p_include_directives','parser_class.py',22),
  ('include_directive -> HASH INCLUDE STRING','include_directive',3,'p_include_directive','parser_class.py',26),
  ('include_directive -> HASH DEFINE ID simple_expression','include_directive',4,'p_include_directive','parser_class.py',27),
  ('declaration_l -> declaration_l declaration','declaration_l',2,'p_declaration_l','parser_class.py',31),
  ('declaration_l -> declaration','declaration_l',1,'p_declaration_l','parser_class.py',32),
  ('declaration -> type var_declaration PUNTOCOMA','declaration',3,'p_declaration','parser_class.py',36),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','parser_class.py',37),
  ('var_declaration -> var_declaration COMA var_definition','var_declaration',3,'p_var_declaration','parser_class.py',43),
  ('var_declaration -> var_definition','var_declaration',1,'p_var_declaration','parser_class.py',44),
  ('var_definition -> ID','var_definition',1,'p_var_definition','parser_class.py',48),
  ('var_definition -> ID ASSIGN simple_expression','var_definition',3,'p_var_definition','parser_class.py',49),
  ('fun_declaration -> type ID LPAREN params RPAREN compound_stmt','fun_declaration',6,'p_fun_declaration','parser_class.py',53),
  ('fun_declaration -> VOID ID LPAREN params RPAREN compound_stmt','fun_declaration',6,'p_fun_declaration','parser_class.py',54),
  ('params -> params_l','params',1,'p_params','parser_class.py',58),
  ('params -> VOID','params',1,'p_params','parser_class.py',59),
  ('params -> empty','params',1,'p_params','parser_class.py',60),
  ('params_l -> params_l COMA param','params_l',3,'p_params_l','parser_class.py',64),
  ('params_l -> param','params_l',1,'p_params_l','parser_class.py',65),
  ('param -> type ID','param',2,'p_param','parser_class.py',69),
  ('type -> INT','type',1,'p_type','parser_class.py',72),
  ('type -> FLOAT','type',1,'p_type','parser_class.py',73),
  ('type -> CHAR','type',1,'p_type','parser_class.py',74),
  ('expression -> ID ASSIGN simple_expression','expression',3,'p_expression','parser_class.py',80),
  ('expression -> simple_expression','expression',1,'p_expression','parser_class.py',81),
  ('expression_stmt -> expression PUNTOCOMA','expression_stmt',2,'p_expression_stmt','parser_class.py',85),
  ('expression_stmt -> PUNTOCOMA','expression_stmt',1,'p_expression_stmt','parser_class.py',86),
  ('compound_stmt -> BLOCK_START local_instructions BLOCK_END','compound_stmt',3,'p_compound_stmt','parser_class.py',90),
  ('local_instructions -> local_instructions type var_declaration PUNTOCOMA','local_instructions',4,'p_local_instructions','parser_class.py',94),
  ('local_instructions -> local_instructions statement','local_instructions',2,'p_local_instructions','parser_class.py',95),
  ('local_instructions -> empty','local_instructions',1,'p_local_instructions','parser_class.py',96),
  ('statement -> expression_stmt','statement',1,'p_statement','parser_class.py',100),
  ('statement -> compound_stmt','statement',1,'p_statement','parser_class.py',101),
  ('statement -> if_stmt','statement',1,'p_statement','parser_class.py',102),
  ('statement -> while_stmt','statement',1,'p_statement','parser_class.py',103),
  ('statement -> do_while_stmt','statement',1,'p_statement','parser_class.py',104),
  ('statement -> return_stmt','statement',1,'p_statement','parser_class.py',105),
  ('statement -> lectura_stm','statement',1,'p_statement','parser_class.py',106),
  ('statement -> escritura_stm','statement',1,'p_statement','parser_class.py',107),
  ('return_stmt -> RETURN PUNTOCOMA','return_stmt',2,'p_return_stmt','parser_class.py',111),
  ('return_stmt -> RETURN expression PUNTOCOMA','return_stmt',3,'p_return_stmt','parser_class.py',112),
  ('if_stmt -> IF LPAREN condition RPAREN statement','if_stmt',5,'p_if_stmt','parser_class.py',116),
  ('if_stmt -> IF LPAREN condition RPAREN statement ELSE statement','if_stmt',7,'p_if_stmt','parser_class.py',117),
  ('while_stmt -> WHILE LPAREN condition RPAREN statement','while_stmt',5,'p_while_stmt','parser_class.py',121),
  ('do_while_stmt -> DO statement','do_while_stmt',2,'p_do_while_stmt','parser_class.py',124),
  ('condition -> NEGATION simple_expression','condition',2,'p_condition','parser_class.py',134),
  ('condition -> condition LOGIC_OP simple_expression','condition',3,'p_condition','parser_class.py',135),
  ('condition -> simple_expression','condition',1,'p_condition','parser_class.py',136),
  ('simple_expression -> simple_expression RELATION_OP bit_operation','simple_expression',3,'p_simple_expression','parser_class.py',141),
  ('simple_expression -> bit_operation','simple_expression',1,'p_simple_expression','parser_class.py',142),
  ('bit_operation -> bit_operation BIT_OP additive_operation','bit_operation',3,'p_bit_operation','parser_class.py',146),
  ('bit_operation -> additive_operation','bit_operation',1,'p_bit_operation','parser_class.py',147),
  ('additive_operation -> additive_operation ARITMETIC_OP_ADD prod_operation','additive_operation',3,'p_additive_operation','parser_class.py',151),
  ('additive_operation -> prod_operation','additive_operation',1,'p_additive_operation','parser_class.py',152),
  ('prod_operation -> prod_operation ARITMETIC_OP_PROD factor','prod_operation',3,'p_prod_operation','parser_class.py',156),
  ('prod_operation -> factor','prod_operation',1,'p_prod_operation','parser_class.py',157),
  ('factor -> LPAREN simple_expression RPAREN','factor',3,'p_factor','parser_class.py',161),
  ('factor -> call','factor',1,'p_factor','parser_class.py',162),
  ('factor -> ID','factor',1,'p_factor','parser_class.py',163),
  ('factor -> NUMBER','factor',1,'p_factor','parser_class.py',164),
  ('factor -> CHARACTER','factor',1,'p_factor','parser_class.py',165),
  ('escritura_stm -> ESCRITURA LPAREN STRING COMA var_multiple RPAREN PUNTOCOMA','escritura_stm',7,'p_escritura','parser_class.py',168),
  ('escritura_stm -> ESCRITURA LPAREN STRING RPAREN PUNTOCOMA statement','escritura_stm',6,'p_escritura','parser_class.py',169),
  ('lectura_stm -> LECTURA LPAREN COMILLA_DOBLE modificadores COMILLA_DOBLE COMA var_multiple RPAREN PUNTOCOMA statement','lectura_stm',10,'p_lectura','parser_class.py',172),
  ('var_multiple -> ID','var_multiple',1,'p_var_multiple','parser_class.py',176),
  ('var_multiple -> ID COMA var_multiple','var_multiple',3,'p_var_multiple','parser_class.py',177),
  ('modificadores -> MODIFICADOR','modificadores',1,'p_multiple_modificador','parser_class.py',180),
  ('modificadores -> MODIFICADOR modificadores','modificadores',2,'p_multiple_modificador','parser_class.py',181),
  ('call -> ID LPAREN args RPAREN','call',4,'p_call','parser_class.py',186),
  ('args -> args_l','args',1,'p_args','parser_class.py',189),
  ('args -> empty','args',1,'p_args','parser_class.py',190),
  ('args_l -> args_l COMA simple_expression','args_l',3,'p_args_l','parser_class.py',194),
  ('args_l -> simple_expression','args_l',1,'p_args_l','parser_class.py',195),
]
