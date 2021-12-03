import ply.yacc as yacc
import os
import codecs
import re
from sys import stdin
from lexer import tokens

def p_program(p):
    '''program : include_directives blocks_code
                | comentario comentario_bloque include_directives blocks_code
    '''
    
def p_empty(p):
    'empty :'
    pass

def p_include_directives(p):
    '''include_directives : include_directives include
                        | include
                        | empty
    '''

def p_include(p):
    '''include : HASH INCLUDE LIBRERIA
                | HASH INCLUDE MENOR identificador MAYOR
                | HASH DEFINE identificador NUMERO
                | HASH DEFINE identificador STRING
    '''

def p_blocks_code(p):
    '''blocks_code : blocks_code funtion
                    | funtion
                    | init_funtion
                    | empty
    '''

def p_funtion(p):
    '''funtion : DATATYPE identificador LPAREN params RPAREN BBLOCK instruction RETURN identificador SEMICOLON EBLOCK blocks_code
        | DATATYPE identificador LPAREN params RPAREN BBLOCK instruction RETURN NUMERO SEMICOLON EBLOCK blocks_code
        | VOID identificador LPAREN params RPAREN BBLOCK instruction EBLOCK blocks_code
        | VOID identificador LPAREN params RPAREN BBLOCK instruction RETURN SEMICOLON EBLOCK blocks_code
    '''

def p_lectura(p):
    "lectura : LECTURA LPAREN COMILLA_DOBLE modificadores COMILLA_DOBLE COMA var_multiple RPAREN SEMICOLON instruction"

def p_modificadores(p):
    '''modificadores : MODIFICADOR modificadores
                        | MODIFICADOR
    '''

def p_escritura(p):
    ''' escritura : ESCRITURA LPAREN STRING COMA var_multiple RPAREN SEMICOLON
            | ESCRITURA LPAREN STRING RPAREN SEMICOLON instruction '''

def p_var_multiple(p):
    ''' var_multiple : identificador
                        | identificador COMA var_multiple
    '''

def p_llamada_funtion(p):
    '''llamada_funtion : identificador LPAREN params2 RPAREN SEMICOLON
                        | identificador LPAREN params2 RPAREN SEMICOLON instruction
    '''

def p_init_funtion(p):
    '''init_funtion : DATATYPE identificador LPAREN params RPAREN SEMICOLON
                | DATATYPE identificador LPAREN params RPAREN SEMICOLON blocks_code'''

def p_params2(p):
    '''params2 : param2
                | empty
    '''

def p_param2(p):
    '''param2 : identificador
                | STRING
                | NUMERO
                | STRING COMA param2
                | NUMERO COMA param2
                | identificador COMA param2
    '''

def p_params(p):
    '''params : param
                | empty
    '''

def p_param(p):
    '''param : DATATYPE identificador
            | DATATYPE identificador COMA param
    '''

def p_instruction(p): 
    '''instruction : var_declaracion SEMICOLON instruction
                    | llamada_funtion
                    | init_funtion
                    | if
                    | while
                    | lectura
                    | escritura
                    | aritmetica
                    | asignacion
                    | operacion
                    | empty
    '''

def p_while(p):
    '''while : WHILE LPAREN conditions RPAREN BBLOCK instruction EBLOCK
            | WHILE LPAREN conditions RPAREN BBLOCK instruction EBLOCK instruction
    '''

def p_conditions(p):
    '''conditions : identificador RELATIONAL identificador
            | identificador RELATIONAL identificador LOGIC conditions
            | identificador MAYOR identificador
            | identificador MAYOR identificador LOGIC conditions
            | identificador MENOR identificador
            | identificador MENOR identificador LOGIC conditions
            | identificador
            | identificador LOGIC conditions
            | BOOL
            | BOOL LOGIC conditions
    '''

def p_if(p):
    '''if : IF LPAREN conditions RPAREN BBLOCK instruction EBLOCK
        | IF LPAREN conditions RPAREN BBLOCK instruction EBLOCK instruction
        | IF LPAREN conditions RPAREN BBLOCK instruction EBLOCK else
    '''

def p_else(p):
    '''else : ELSE BBLOCK instruction EBLOCK
            | ELSE BBLOCK instruction EBLOCK instruction '''

def p_var_declaracion(p):
    '''var_declaracion : DATATYPE identificador
                        | DATATYPE just_id
    '''

def p_just_id(p):
    '''just_id : identificador
                | identificador COMA just_id
                | identificador IGUAL NUMERO 
                | identificador IGUAL NUMERO COMA just_id
    '''

def p_asignacion(p):
    '''asignacion : DATATYPE identificador IGUAL aritmetica SEMICOLON instruction
                | identificador IGUAL aritmetica SEMICOLON instruction
                | DATATYPE identificador IGUAL identificador SEMICOLON instruction
                | identificador IGUAL identificador SEMICOLON instruction
                | DATATYPE identificador IGUAL operacion_LOGIC SEMICOLON instruction
                | identificador IGUAL operacion_LOGIC SEMICOLON instruction
                | DATATYPE identificador IGUAL operacion SEMICOLON instruction
                | identificador IGUAL operacion SEMICOLON instruction
                | DATATYPE identificador IGUAL STRING SEMICOLON instruction
                | identificador IGUAL STRING SEMICOLON instruction
    '''

def p_aritmetica(p):
    "aritmetica : operacion SEMICOLON instruction"

def p_operacion(p):
    '''operacion : identificador operadores operacion
                | identificador
    '''

def p_operacion_LOGIC(p):
    '''operacion_LOGIC : identificador LOGIC operacion_LOGIC
                        | identificador
    '''
def p_error(p):
    if p:
        print("Syntax error at " + str(p.value) + ", line: " + str(p.lineno))
        parser.errok()
    else:
        print("Error de sintaxis al final del archivo.")

parser = yacc.yacc()

while True:
    code = None
    try:
        s = input('Nombre del archivo: ')
        codeFile = open(s, "r")
        code = codeFile.read()
    except EOFError:
        break
    except IOError:
        print("No file found")
    if code == None or not code:
        continue
    result = parser.parse(code,tracking=True)
    print("Analisis sintactico terminado")