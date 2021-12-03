import ply.lex as lex

tipos = {
  'int': 'INT',
  'float': 'FLOAT',
  'char': 'CHAR',
  'scanf' : 'LECTURA',
  'printf':'ESCRITURA',
}

tokens = [
    'NUMERO',
    'OPERADORES',
    'IDENTIFICADOR',
    'COMA',
    # 'DATATYPE',
    'SEMICOLON',
    'IGUAL',
    'LPAREN',
    'RPAREN',
    'BBLOCK',
    'EBLOCK',
    'LOGIC',
    'RELATIONAL',
    'WHILE',
    'BOOL',
    #'LECTURA',
    'MODIFICADOR',
    #'ESCRITURA',
    'COMILLAS_DOBLES',
    'STRING',
    # 'CARACTER',
    # 'CHAR'
    'EOF'
] + list(tipos.values())

def t_comentario(t):
    r'\/\/.*'
    pass

def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    pass

t_ignore  = ' \t'
t_SEMICOLON = r'\;'
t_IGUAL = r'\='
t_COMA= r'\,'
# t_STRING = r'"(.*?)"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BBLOCK = r'\{'
t_EBLOCK = r'\}'
t_COMILLAS_DOBLES = r'\"'
t_EOF = r'\$'

# def t_DATATYPE(t):
#     r'(INT)|(FLOAT)|(CHAR)'
#     return t

def t_STRING(t):
    r'"(.*?)"'
    return t
    
def t_WHILE(t):
    r'(while)'
    return t

def t_BOOL(t):
    r'(true)|(false)'
    return t

def t_IDENTIFICADOR(t):
    r'([a-z]|[A-Z]|_*([a-z]|[A-Z]))([a-z]|[A-Z]|\d|_)*'
    t.type = tipos.get(t.value,'IDENTIFICADOR')
    return t

def t_NUMERO(t):
    r'(\d)+(\.(\d)+)?'
    if ("." in t.value):
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_RELATIONAL(t):
    r'(\&{2})|(\|{2})'
    return t

def t_LOGIC(t):
    r'(\>=)|(\<=)|(\==)|(\!=)|(\<)|(\>)'
    return t

def t_OPERADORES(t):
    r'(\+)|(\-)|(\*)|(\/)|(\%)'
    return t

def t_error(t):
    print("Caracter no aceptado '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t

# def t_LECTURA(t):
#     r'(scanf)'
#     return t

def t_MODIFICADOR(t):
    r'(%c)|(%d)|(%u)|(%o)|(%x)|(%e)|(%f)|(%s)|(%p)'
    # t.type = tipos.get(t.value,'IDENTIFICADOR')
    return t

# def t_ESCRITURA(t):
#     r"(printf)"
#     return t

lexer = lex.lex()

instrucciones = 0
var_declaracion = 1
aux_var_declaracion = 2
aux_add_declaracion = 3
aux_var_asignacion = 4
while_op = 5
condiciones = 6
conexion_bool_logic = 7
bool_logic = 8
conexion_logica = 9
operacion = 10
aux_operacion = 11
scanf = 12
printf = 13
aux_printf = 14
add_modificadores = 15
aux_modificadores = 16
add_identificadores = 17
aux_identificadores = 18
#bool_type = 19
datatype = 19
#relaciones = 21
#identificador = 22
dato = 20

tabla = [
  # 1
  [instrucciones, 'SEMICOLON', None],
  [instrucciones, 'COMA', None],
  [instrucciones, 'WHILE', [while_op, instrucciones]],
  [instrucciones, 'LPAREN', None],
  [instrucciones, 'RPAREN', None],
  [instrucciones, 'BBLOCK', None],
  [instrucciones, 'EBLOCK', ['empty']],
  [instrucciones, 'LECTURA', [scanf, 'SEMICOLON', instrucciones]],
  [instrucciones, 'COMILLAS_DOBLES', None],
  [instrucciones, 'ESCRITURA', [printf, 'SEMICOLON', instrucciones]],
  [instrucciones, 'BOOL', None],
  [instrucciones, 'LOGIC', None],
  [instrucciones, 'IGUAL', None],
  [instrucciones, 'INT', [var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'FLOAT', [var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'CHAR', [var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'RELATIONAL', None],
  [instrucciones, 'OPERADORES', None],
  [instrucciones, 'MODIFICADOR', None],
  [instrucciones, 'IDENTIFICADOR', [aux_var_declaracion, 'SEMICOLON', instrucciones]],
  [instrucciones, 'STRING', None],
  [instrucciones, 'NUMERO', None],
  [instrucciones, 'EOF', ['empty']],
  # 2
  [var_declaracion, 'SEMICOLON', None],
  [var_declaracion, 'COMA', None],
  [var_declaracion, 'WHILE', None],
  [var_declaracion, 'LPAREN', None],
  [var_declaracion, 'RPAREN', None],
  [var_declaracion, 'BBLOCK', None],
  [var_declaracion, 'EBLOCK', None],
  [var_declaracion, 'LECTURA', None],
  [var_declaracion, 'COMILLAS_DOBLES', None],
  [var_declaracion, 'ESCRITURA', None],
  [var_declaracion, 'BOOL', None],
  [var_declaracion, 'LOGIC', None],
  [var_declaracion, 'IGUAL', None],
  [var_declaracion, 'INT', [datatype, aux_var_declaracion]],
  [var_declaracion, 'FLOAT', [datatype, aux_var_declaracion]],
  [var_declaracion, 'CHAR', [datatype, aux_var_declaracion]],
  [var_declaracion, 'RELATIONAL', None],
  [var_declaracion, 'OPERADORES', None],
  [var_declaracion, 'MODIFICADOR', None],
  [var_declaracion, 'IDENTIFICADOR', None],
  [var_declaracion, 'STRING', None],
  [var_declaracion, 'NUMERO', None],
  [var_declaracion, 'EOF', None],
  # 3
  [aux_var_declaracion, 'SEMICOLON', None ],
  [aux_var_declaracion,  'COMA', None ],
  [aux_var_declaracion, 'WHILE', None ],
  [aux_var_declaracion, 'LPAREN', None],
  [aux_var_declaracion, 'RPAREN', None ],
  [aux_var_declaracion, 'BBLOCK', None ],
  [aux_var_declaracion, 'EBLOCK', None ],
  [aux_var_declaracion, 'LECTURA', None ],
  [aux_var_declaracion, 'COMILLAS_DOBLES', None ],
  [aux_var_declaracion, 'ESCRITURA', None ],
  [aux_var_declaracion, 'BOOL', None ],
  [aux_var_declaracion, 'LOGIC', None ],
  [aux_var_declaracion, 'IGUAL', None ],
  [aux_var_declaracion, 'INT', None ],
  [aux_var_declaracion, 'FLOAT', None ],
  [aux_var_declaracion, 'CHAR', None ],
  [aux_var_declaracion, 'RELATIONAL', None ],
  [aux_var_declaracion, 'OPERADORES', None ],
  [aux_var_declaracion, 'MODIFICADOR', None ],
  [aux_var_declaracion, 'IDENTIFICADOR', ['IDENTIFICADOR', aux_var_asignacion, aux_add_declaracion]],
  [aux_var_declaracion, 'STRING', None ],
  [aux_var_declaracion, 'NUMERO', None],
  [aux_var_declaracion, 'EOF', None ],
  #4
  [aux_add_declaracion, 'SEMICOLON', ['empty']],
  [aux_add_declaracion, 'COMA', ['COMA', aux_var_declaracion]],
  [aux_add_declaracion, 'WHILE', None],
  [aux_add_declaracion, 'LPAREN', None],
  [aux_add_declaracion, 'RPAREN', None],
  [aux_add_declaracion, 'BBLOCK', None],
  [aux_add_declaracion, 'EBLOCK', None],
  [aux_add_declaracion, 'LECTURA', None],
  [aux_add_declaracion, 'COMILLAS_DOBLES', None],
  [aux_add_declaracion, 'ESCRITURA', None],
  [aux_add_declaracion, 'BOOL', None],
  [aux_add_declaracion, 'LOGIC', None],
  [aux_add_declaracion, 'IGUAL', None],
  [aux_add_declaracion, 'INT', None],
  [aux_add_declaracion, 'FLOAT', None],
  [aux_add_declaracion, 'CHAR', None],
  [aux_add_declaracion, 'RELATIONAL', None],
  [aux_add_declaracion, 'OPERADORES', None],
  [aux_add_declaracion, 'MODIFICADOR', None],
  [aux_add_declaracion, 'IDENTIFICADOR', None],
  [aux_add_declaracion, 'STRING', None],
  [aux_add_declaracion, 'NUMERO', None],
  [aux_add_declaracion, 'EOF', None],
  #5
  [aux_var_asignacion,'SEMICOLON', ['empty']],
  [aux_var_asignacion,  'COMA', ['empty']],
  [aux_var_asignacion, 'WHILE', None],
  [aux_var_asignacion, 'LPAREN', None],
  [aux_var_asignacion, 'RPAREN', None],
  [aux_var_asignacion, 'BBLOCK', None],
  [aux_var_asignacion, 'EBLOCK', None],
  [aux_var_asignacion, 'LECTURA', None],
  [aux_var_asignacion, 'COMILLAS_DOBLES', None],
  [aux_var_asignacion, 'ESCRITURA', None],
  [aux_var_asignacion, 'BOOL', None],
  [aux_var_asignacion, 'LOGIC', None],
  [aux_var_asignacion, 'IGUAL', ['IGUAL', dato]],
  [aux_var_asignacion, 'INT', None],
  [aux_var_asignacion, 'FLOAT',None],
  [aux_var_asignacion, 'CHAR', None],
  [aux_var_asignacion, 'RELATIONAL', None],
  [aux_var_asignacion, 'OPERADORES', None],
  [aux_var_asignacion, 'MODIFICADOR', None],
  [aux_var_asignacion, 'IDENTIFICADOR', None],
  [aux_var_asignacion, 'STRING', None],
  [aux_var_asignacion, 'NUMERO', None],
  [aux_var_asignacion, 'EOF', None],
  #6
  [while_op, 'SEMICOLON', None],
  [while_op, 'COMA', None],
  [while_op, 'WHILE', ['WHILE','LPAREN' , condiciones, 'RPAREN' , 'BBLOCK', instrucciones, 'EBLOCK']],
  [while_op, 'LPAREN', None],
  [while_op, 'RPAREN', None],
  [while_op, 'BBLOCK', None],
  [while_op, 'EBLOCK', None],
  [while_op, 'LECTURA', None],
  [while_op, 'COMILLAS_DOBLES',None],
  [while_op, 'ESCRITURA', None],
  [while_op, 'BOOL',None ],
  [while_op, 'LOGIC', None],
  [while_op, 'IGUAL', None],
  [while_op, 'INT',None ],
  [while_op, 'FLOAT',None ],
  [while_op, 'CHAR',None ],
  [while_op, 'RELATIONAL',None ],
  [while_op, 'OPERADORES', None],
  [while_op, 'MODIFICADOR',None ],
  [while_op, 'IDENTIFICADOR', None],
  [while_op, 'STRING', None],
  [while_op, 'NUMERO', None],
  [while_op, 'EOF',None ],
  #7
  [condiciones, 'SEMICOLON', None],
  [condiciones, 'COMA', None],
  [condiciones, 'WHILE', None],
  [condiciones, 'LPAREN', None],
  [condiciones, 'RPAREN', None],
  [condiciones, 'BBLOCK', None],
  [condiciones, 'EBLOCK', None],
  [condiciones, 'LECTURA', None],
  [condiciones, 'COMILLAS_DOBLES', None],
  [condiciones, 'ESCRITURA', None],
  [condiciones, 'BOOL', [bool_logic, conexion_bool_logic]],
  [condiciones, 'LOGIC', None],
  [condiciones, 'IGUAL', None],
  [condiciones, 'INT', None],
  [condiciones, 'FLOAT', None],
  [condiciones, 'CHAR', None],
  [condiciones, 'RELATIONAL', None],
  [condiciones, 'OPERADORES', None],
  [condiciones, 'MODIFICADOR', None],
  [condiciones, 'IDENTIFICADOR', [bool_logic, conexion_bool_logic]],
  [condiciones, 'STRING', None],
  [condiciones, 'NUMERO', None],
  [condiciones, 'EOF', None],
  #8
  [conexion_bool_logic, 'SEMICOLON', None],
  [conexion_bool_logic, 'COMA', None],
  [conexion_bool_logic, 'WHILE', None],
  [conexion_bool_logic, 'LPAREN', None],
  [conexion_bool_logic, 'RPAREN', ['empty']],
  [conexion_bool_logic, 'BBLOCK', None],
  [conexion_bool_logic, 'EBLOCK', None],
  [conexion_bool_logic, 'LECTURA', None],
  [conexion_bool_logic, 'COMILLAS_DOBLES', None],
  [conexion_bool_logic, 'ESCRITURA', None],
  [conexion_bool_logic, 'BOOL', None],
  [conexion_bool_logic, 'LOGIC', None],
  [conexion_bool_logic, 'IGUAL', None],
  [conexion_bool_logic, 'INT', None],
  [conexion_bool_logic, 'FLOAT', None],
  [conexion_bool_logic, 'CHAR', None],
  [conexion_bool_logic, 'RELATIONAL', ['RELATIONAL', bool_logic, conexion_bool_logic]],
  [conexion_bool_logic, 'OPERADORES', None],
  [conexion_bool_logic, 'MODIFICADOR', None],
  [conexion_bool_logic, 'IDENTIFICADOR', None],
  [conexion_bool_logic, 'STRING', None],
  [conexion_bool_logic, 'NUMERO', None],
  [conexion_bool_logic, 'EOF', None],
  #9
  [bool_logic, 'SEMICOLON', None],
  [bool_logic, 'COMA', None],
  [bool_logic, 'WHILE', None],
  [bool_logic, 'LPAREN', None],
  [bool_logic, 'RPAREN', None],
  [bool_logic, 'BBLOCK', None],
  [bool_logic, 'EBLOCK', None],
  [bool_logic, 'LECTURA', None],
  [bool_logic, 'COMILLAS_DOBLES', None],
  [bool_logic, 'ESCRITURA', None],
  [bool_logic, 'BOOL', ['BOOL']],
  [bool_logic, 'LOGIC', None],
  [bool_logic, 'IGUAL', None],
  [bool_logic, 'INT', None],
  [bool_logic, 'FLOAT', None],
  [bool_logic, 'CHAR', None],
  [bool_logic, 'RELATIONAL', None],
  [bool_logic, 'OPERADORES', None],
  [bool_logic, 'MODIFICADOR', None],
  [bool_logic, 'IDENTIFICADOR', ['IDENTIFICADOR', conexion_logica]],
  [bool_logic, 'STRING', None],
  [bool_logic, 'NUMERO', None],
  [bool_logic, 'EOF', None],
  #10
  [conexion_logica, 'SEMICOLON', None],
  [conexion_logica, 'COMA', None],
  [conexion_logica, 'WHILE', None],
  [conexion_logica, 'LPAREN', None],
  [conexion_logica, 'RPAREN', ['empty']],
  [conexion_logica, 'BBLOCK', None],
  [conexion_logica, 'EBLOCK', None],
  [conexion_logica, 'LECTURA', None],
  [conexion_logica, 'COMILLAS_DOBLES', None],
  [conexion_logica, 'ESCRITURA', None],
  [conexion_logica, 'BOOL', None],
  [conexion_logica, 'LOGIC', ['LOGIC' , 'IDENTIFICADOR']],
  [conexion_logica, 'IGUAL', None],
  [conexion_logica, 'INT', None],
  [conexion_logica, 'FLOAT', None],
  [conexion_logica, 'CHAR', None],
  [conexion_logica, 'RELATIONAL', ['empty']],
  [conexion_logica, 'OPERADORES', None],
  [conexion_logica, 'MODIFICADOR', None],
  [conexion_logica, 'IDENTIFICADOR', None],
  [conexion_logica, 'STRING', None],
  [conexion_logica, 'NUMERO', None],
  [conexion_logica, 'EOF', None],
  #11
  [operacion, 'SEMICOLON',None ],
  [operacion, 'COMA',None ],
  [operacion, 'WHILE',None ],
  [operacion, 'LPAREN', None],
  [operacion, 'RPAREN', None],
  [operacion, 'BBLOCK', None],
  [operacion, 'EBLOCK', None],
  [operacion, 'LECTURA', None],
  [operacion, 'COMILLAS_DOBLES', None],
  [operacion, 'ESCRITURA', None],
  [operacion, 'BOOL', None],
  [operacion, 'LOGIC', None],
  [operacion, 'IGUAL', None],
  [operacion, 'INT',None ],
  [operacion, 'FLOAT',None ],
  [operacion, 'CHAR',None ],
  [operacion, 'RELATIONAL',None ],
  [operacion, 'OPERADORES', None],
  [operacion, 'MODIFICADOR',None ],
  [operacion, 'IDENTIFICADOR', ['IDENTIFICADOR','OPERADORES','IDENTIFICADOR',aux_operacion]],
  [operacion, 'STRING', None],
  [operacion, 'NUMERO', None],
  [operacion, 'EOF', None],
  #12
  [aux_operacion, 'SEMICOLON', ['empty']],
  [aux_operacion, 'COMA', ['empty']],
  [aux_operacion, 'WHILE', None],
  [aux_operacion, 'LPAREN', None],
  [aux_operacion, 'RPAREN', None],
  [aux_operacion, 'BBLOCK', None],
  [aux_operacion, 'EBLOCK', None],
  [aux_operacion, 'LECTURA', None],
  [aux_operacion, 'COMILLAS_DOBLES', None],
  [aux_operacion, 'ESCRITURA', None],
  [aux_operacion, 'BOOL', None],
  [aux_operacion, 'LOGIC', None],
  [aux_operacion, 'IGUAL', None],
  [aux_operacion, 'INT', None],
  [aux_operacion, 'FLOAT', None],
  [aux_operacion, 'CHAR', None],
  [aux_operacion, 'RELATIONAL', None],
  [aux_operacion, 'OPERADORES', ['OPERADORES', 'IDENTIFICADOR', aux_operacion]],
  [aux_operacion, 'MODIFICADOR', None],
  [aux_operacion, 'IDENTIFICADOR', None],
  [aux_operacion, 'STRING', None],
  [aux_operacion, 'NUMERO', None],
  [aux_operacion, 'EOF', None],
  #13
  [scanf, 'SEMICOLON', None],
  [scanf, 'COMA', None],
  [scanf, 'WHILE', None],
  [scanf, 'LPAREN', None],
  [scanf, 'RPAREN', None],
  [scanf, 'BBLOCK', None],
  [scanf, 'EBLOCK', None],
  [scanf, 'LECTURA', ['LECTURA', 'LPAREN', 'STRING', 'COMA', add_identificadores, 'RPAREN']],
  [scanf, 'COMILLAS_DOBLES', None],
  [scanf, 'ESCRITURA', None],
  [scanf, 'BOOL', None],
  [scanf, 'LOGIC', None],
  [scanf, 'IGUAL', None],
  [scanf, 'INT', None],
  [scanf, 'FLOAT', None],
  [scanf, 'CHAR', None],
  [scanf, 'RELATIONAL', None],
  [scanf, 'OPERADORES', None],
  [scanf, 'MODIFICADOR', None],
  [scanf, 'IDENTIFICADOR', None],
  [scanf, 'STRING', None],
  [scanf, 'NUMERO', None],
  [scanf, 'EOF', None],
  #14
  [printf, 'SEMICOLON', None],
  [printf, 'COMA', None],
  [printf, 'WHILE', None],
  [printf, 'LPAREN', None],
  [printf, 'RPAREN', None],
  [printf, 'BBLOCK', None],
  [printf, 'EBLOCK', None],
  [printf, 'LECTURA', None],
  [printf, 'COMILLAS_DOBLES',None ],
  [printf, 'ESCRITURA', ['ESCRITURA', 'LPAREN','STRING', aux_printf,'RPAREN']],
  [printf, 'BOOL',None ],
  [printf, 'LOGIC', None],
  [printf, 'IGUAL', None],
  [printf, 'INT',None ],
  [printf, 'FLOAT',None ],
  [printf, 'CHAR',None ],
  [printf, 'RELATIONAL',None ],
  [printf, 'OPERADORES', None],
  [printf, 'MODIFICADOR',None ],
  [printf, 'IDENTIFICADOR', None],
  [printf, 'STRING', None],
  [printf, 'NUMERO', None],
  [printf, 'EOF',None ],
  #15
  [aux_printf, 'SEMICOLON', None],
  [aux_printf, 'COMA', ['COMA', add_identificadores]],
  [aux_printf, 'WHILE', None],
  [aux_printf, 'LPAREN', None],
  [aux_printf, 'RPAREN', ['empty']],
  [aux_printf, 'BBLOCK', None],
  [aux_printf, 'EBLOCK', None],
  [aux_printf, 'LECTURA', None],
  [aux_printf, 'COMILLAS_DOBLES', None],
  [aux_printf, 'ESCRITURA', None],
  [aux_printf, 'BOOL', None],
  [aux_printf, 'LOGIC', None],
  [aux_printf, 'IGUAL', None],
  [aux_printf, 'INT', None],
  [aux_printf, 'FLOAT', None],
  [aux_printf, 'CHAR', None],
  [aux_printf, 'RELATIONAL', None],
  [aux_printf, 'OPERADORES', None],
  [aux_printf, 'MODIFICADOR', None],
  [aux_printf, 'IDENTIFICADOR', None],
  [aux_printf, 'STRING', None],
  [aux_printf, 'NUMERO', None],
  [aux_printf, 'EOF', None],
  #16
  [add_modificadores, 'SEMICOLON', None],
  [add_modificadores, 'COMA', None],
  [add_modificadores, 'WHILE', None],
  [add_modificadores, 'LPAREN', None],
  [add_modificadores, 'RPAREN', None],
  [add_modificadores, 'BBLOCK', None],
  [add_modificadores, 'EBLOCK', None],
  [add_modificadores, 'LECTURA', None],
  [add_modificadores, 'COMILLAS_DOBLES', None],
  [add_modificadores, 'ESCRITURA', None],
  [add_modificadores, 'BOOL', None],
  [add_modificadores, 'LOGIC', None],
  [add_modificadores, 'IGUAL', None],
  [add_modificadores, 'INT', None],
  [add_modificadores, 'FLOAT', None],
  [add_modificadores, 'CHAR', None],
  [add_modificadores, 'RELATIONAL', None],
  [add_modificadores, 'OPERADORES', None],
  [add_modificadores, 'MODIFICADOR', ['MODIFICADOR', aux_modificadores]],
  [add_modificadores, 'IDENTIFICADOR', None],
  [add_modificadores, 'STRING', None],
  [add_modificadores, 'NUMERO', None],
  [add_modificadores, 'EOF', None],
  #17
  [aux_modificadores, 'SEMICOLON', None],
  [aux_modificadores, 'COMA', None],
  [aux_modificadores, 'WHILE', None],
  [aux_modificadores, 'LPAREN', None],
  [aux_modificadores, 'RPAREN', None],
  [aux_modificadores, 'BBLOCK', None],
  [aux_modificadores, 'EBLOCK', None],
  [aux_modificadores, 'LECTURA', None],
  [aux_modificadores, 'COMILLAS_DOBLES', ['empty']],
  [aux_modificadores, 'ESCRITURA', None],
  [aux_modificadores, 'BOOL', None],
  [aux_modificadores, 'LOGIC', None],
  [aux_modificadores, 'IGUAL', None],
  [aux_modificadores, 'INT', None],
  [aux_modificadores, 'FLOAT', None],
  [aux_modificadores, 'CHAR', None],
  [aux_modificadores, 'RELATIONAL', None],
  [aux_modificadores, 'OPERADORES', None],
  [aux_modificadores, 'MODIFICADOR', ['MODIFICADOR', aux_modificadores]],
  [aux_modificadores, 'IDENTIFICADOR', None],
  [aux_modificadores, 'STRING', None],
  [aux_modificadores, 'NUMERO', None],
  [aux_modificadores, 'EOF', None],
  #18
  [add_identificadores, 'SEMICOLON', None],
  [add_identificadores, 'COMA', None],
  [add_identificadores, 'WHILE', None],
  [add_identificadores, 'LPAREN', None],
  [add_identificadores, 'RPAREN', None],
  [add_identificadores, 'BBLOCK', None],
  [add_identificadores, 'EBLOCK', None],
  [add_identificadores, 'LECTURA', None],
  [add_identificadores, 'COMILLAS_DOBLES', None],
  [add_identificadores, 'ESCRITURA', None],
  [add_identificadores, 'BOOL', None],
  [add_identificadores, 'LOGIC', None],
  [add_identificadores, 'IGUAL', None],
  [add_identificadores, 'INT', None],
  [add_identificadores, 'FLOAT', None],
  [add_identificadores, 'CHAR', None],
  [add_identificadores, 'RELATIONAL', None],
  [add_identificadores, 'OPERADORES', None],
  [add_identificadores, 'MODIFICADOR', None],
  [add_identificadores, 'IDENTIFICADOR', ['IDENTIFICADOR', aux_identificadores]],
  [add_identificadores, 'STRING', None],
  [add_identificadores, 'NUMERO', None],
  [add_identificadores, 'EOF', None],
  #19
  [aux_identificadores, 'SEMICOLON',None ],
  [aux_identificadores, 'COMA',['COMA','IDENTIFICADOR',aux_identificadores] ],
  [aux_identificadores, 'WHILE',None ],
  [aux_identificadores, 'LPAREN', None],
  [aux_identificadores, 'RPAREN', ['empty']],
  [aux_identificadores, 'BBLOCK', None],
  [aux_identificadores, 'EBLOCK', None],
  [aux_identificadores, 'LECTURA', None],
  [aux_identificadores, 'COMILLAS_DOBLES', None],
  [aux_identificadores, 'ESCRITURA', None],
  [aux_identificadores, 'BOOL', None],
  [aux_identificadores, 'LOGIC', None],
  [aux_identificadores, 'IGUAL', None],
  [aux_identificadores, 'INT',None ],
  [aux_identificadores, 'FLOAT',None ],
  [aux_identificadores, 'CHAR',None ],
  [aux_identificadores, 'RELATIONAL',None ],
  [aux_identificadores, 'OPERADORES', None],
  [aux_identificadores, 'MODIFICADOR',None ],
  [aux_identificadores, 'IDENTIFICADOR', None],
  [aux_identificadores, 'STRING', None],
  [aux_identificadores, 'NUMERO', None],
  [aux_identificadores, 'EOF', None],
  #20
  [datatype, 'SEMICOLON', None],
  [datatype, 'COMA', None],
  [datatype, 'WHILE', None],
  [datatype, 'LPAREN', None],
  [datatype, 'RPAREN', None],
  [datatype, 'BBLOCK', None],
  [datatype, 'EBLOCK', None],
  [datatype, 'LECTURA', None],
  [datatype, 'COMILLAS_DOBLES', None],
  [datatype, 'ESCRITURA', None],
  [datatype, 'BOOL', None],
  [datatype, 'LOGIC', None],
  [datatype, 'IGUAL', None],
  [datatype, 'INT', ['INT']],
  [datatype, 'FLOAT', ['FLOAT']],
  [datatype, 'CHAR', ['CHAR']],
  [datatype, 'RELATIONAL', None],
  [datatype, 'OPERADORES', None],
  [datatype, 'MODIFICADOR', None],
  [datatype, 'IDENTIFICADOR', None],
  [datatype, 'STRING', None],
  [datatype, 'NUMERO', None],
  [datatype, 'EOF', None],
  #21
  [dato, 'SEMICOLON', None],
  [dato, 'COMA', None],
  [dato, 'WHILE', None],
  [dato, 'LPAREN', None],
  [dato, 'RPAREN', None],
  [dato, 'BBLOCK', None],
  [dato, 'EBLOCK', None],
  [dato, 'LECTURA', None],
  [dato, 'COMILLAS_DOBLES', None],
  [dato, 'ESCRITURA', None],
  [dato, 'BOOL', None],
  [dato, 'LOGIC', None],
  [dato, 'IGUAL', None],
  [dato, 'INT', None],
  [dato, 'FLOAT', None],
  [dato, 'CHAR', None],
  [dato, 'RELATIONAL', None],
  [dato, 'OPERADORES', None],
  [dato, 'MODIFICADOR', None],
  [dato, 'IDENTIFICADOR', [operacion]],
  [dato, 'STRING', ['STRING']],
  [dato, 'NUMERO', ['NUMERO']],
  [dato, 'EOF', None]
]

stack = ['EOF', 0]

def miParser(code):
    f = open('c.c', 'r')
    code = f.read()
    lexer.input(code)    
    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    while True:    
        if x == tok.type and x == 'EOF':
            print("Cadena reconocida exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'EOF':
                stack.pop()
                x=stack[-1]
                tok=lexer.token()                
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                print("En posición:", tok.lexpos)
                print("En linea:", tok.lineno)
                return 0;
            if x not in tokens: #es no terminal
                print("van entrar a la tabla:")
                print(x)
                print(tok.type)
                print("En linea:", tok.lineno)
                celda=buscar_en_tabla(x,tok.type)                            
                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print("En posición:", tok.lexpos)
                    print("En linea:", tok.lineno)
                    print("celda: ", celda)
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("-*-*-*-*-*-*-*-*-*-*-*-")
                    x=stack[-1]            
def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla)):
        if( tabla[i][0] == no_terminal and tabla[i][1] == terminal):
            return tabla[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'empty': #la vacía no la inserta
            stack.append(elemento)

def main():
    try:
        i = input('Datafile > ')
        f = open(i, 'r')
        code = f.read()
        miParser(code)
    except IOError:
        print("File not found")
main()