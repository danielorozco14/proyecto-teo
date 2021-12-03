import ply.lex as lex

# Lista de definicion de tokens
tokens = [
    'NUMERO',
    'operadores',
    'identificador',
    'COMA',
    'DATATYPE',
    'SEMICOLON',
    'IGUAL',
    'HASH',
    'INCLUDE',
    'DEFINE',
    'STRING',
    'MENOR',
    'MAYOR',
    'LIBRERIA',
    'LPAREN',
    'RPAREN',
    'BBLOCK',
    'EBLOCK',
    'LOGIC',
    'RELATIONAL',
    'WHILE',
    'BOOL',
    'comentario',
    'comentario_bloque',
    'IF',
    'ELSE',
    'VOID',
    'RETURN',
    'LECTURA',
    'MODIFICADOR',
    'ESCRITURA',
    'COMILLA_DOBLE',
    # 'CARACTER',
    # 'CHAR'
]

t_ignore  = ' \t'
t_SEMICOLON = r'\;'
t_IGUAL = r'\='
t_COMA= r'\,'
t_HASH= r'\#'
t_STRING = r'"(.*?)"'
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BBLOCK = r'\{'
t_EBLOCK = r'\}'
t_COMILLA_DOBLE = r'\"'

def t_INCLUDE(t):
    r'(include)'
    return t

def t_DEFINE(t):
    r'(define)'
    return t

def t_DATATYPE(t):
    r'(int)|(float)|(char)'
    return t

def t_WHILE(t):
    r'(while)'
    return t

def t_BOOL(t):
    r'(true)|(false)'
    return t

def t_IF(t):
    r'(if)'
    return t

def t_ELSE(t):
    r'(else)'
    return t

def t_VOID(t):
    r'(void)'
    return t

def t_RETURN(t):
    r'(return)'
    return t

def t_identificador(t):
    r'([a-z]|[A-Z]|_*([a-z]|[A-Z]))([a-z]|[A-Z]|\d|_)*'
    return t

def t_LIBRERIA(t):
    r'("[a-zA-Z]+\.h")|(<[a-zA-Z]+\.h>)'
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

def t_LOGIC(t):
    r'(\&{2})|(\|{2})'
    return t

def t_RELATIONAL(t):
    r'(\>=)|(\<=)|(\==)|(\!=)'
    return t

def t_comentario(t):
    r'\/\/.*'
    pass

def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    pass

def t_operadores(t):
    r'(\+)|(\-)|(\*)|(\/)|(\%)'
    return t

def t_error(t):
    print("Caracter no aceptado '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t

def t_LECTURA(t):
    r'(scanf)'
    return t

def t_MODIFICADOR(t):
    r'(%c)|(%d)|(%u)|(%o)|(%x)|(%e)|(%f)|(%s)|(%p)'
    return t

def t_ESCRITURA(t):
    r"(printf)"
    return t

# def t_CHAR(t):
#     r'(char)'
#     return t

# def t_CARACTER(t):
#     r"('.')"
#     return t

lexer = lex.lex()

def miLexer():
    f = open('codigo.c','r')

    lexer.input(f.read())
    linenumber = 0
    while True:
        tok=lexer.token()
        if not tok:
            break
        linea = tok.lineno
        if linea != linenumber:
            continue
        #     print('LINEA #: ', linea, '\n')
        # print(tok.type + ': ', tok.value)
        linenumber = tok.lineno

miLexer()