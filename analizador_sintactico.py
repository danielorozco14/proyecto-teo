import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import analizador

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'SUMA', 'RESTA', 'MULT', 'DIV'),
    ('left', 'CHAR', 'INT', 'FLOAT'),
    ('right', 'UMINUS'),
    ('right', 'PUNTOCOMA'),
    ('left', 'SI'),
    ('right','SINO'),
    ('left', 'PARA'),
    ('left','NUMERAL'),
    ('right','INCLUDE'),
    ('left','PARIZQ' ,'LLAIZQ'),
    ('right','PARDER', 'LLADER')
)
nombres = {}

def p_empty(p):
    'empty :'
    pass

#-----------------------------------------------------------------------------------------------------------------------    
#Declaraciones
def p_declaracion_asignar(t):
    '''
    declaracion_asignar : CHAR IDENTIFICADOR PUNTOCOMA 
                | INT IDENTIFICADOR PUNTOCOMA
                | FLOAT IDENTIFICADOR PUNTOCOMA

                | CHAR IDENTIFICADOR CORIZQ  CORDER PUNTOCOMA 
                | INT IDENTIFICADOR CORIZQ  CORDER PUNTOCOMA 
                | FLOAT IDENTIFICADOR CORIZQ  CORDER PUNTOCOMA

                | CHAR IDENTIFICADOR CORIZQ NUMERO CORDER PUNTOCOMA 
                | INT IDENTIFICADOR CORIZQ NUMERO CORDER PUNTOCOMA 
                | FLOAT IDENTIFICADOR CORIZQ NUMERO CORDER PUNTOCOMA

                | CHAR IDENTIFICADOR COMA declaracion_asignar
                | INT IDENTIFICADOR COMA declaracion_asignar
                | FLOAT IDENTIFICADOR COMA declaracion_asignar

                | CHAR IDENTIFICADOR CORIZQ CORDER COMA declaracion_asignar 
                | INT IDENTIFICADOR CORIZQ  CORDER COMA declaracion_asignar
                | FLOAT IDENTIFICADOR CORIZQ CORDER COMA declaracion_asignar

                | CHAR IDENTIFICADOR CORIZQ NUMERO CORDER COMA declaracion_asignar 
                | INT IDENTIFICADOR CORIZQ  NUMERO CORDER COMA declaracion_asignar
                | FLOAT IDENTIFICADOR CORIZQ NUMERO CORDER COMA declaracion_asignar

                | IDENTIFICADOR COMA declaracion_asignar
                | IDENTIFICADOR PUNTOCOMA

                | IDENTIFICADOR CORIZQ CORDER COMA declaracion_asignar
                | IDENTIFICADOR CORIZQ CORDER PUNTOCOMA

                | IDENTIFICADOR CORIZQ NUMERO CORDER COMA declaracion_asignar
                | IDENTIFICADOR CORIZQ NUMERO CORDER PUNTOCOMA

                | INT IDENTIFICADOR ASIGNAR NUMERO PUNTOCOMA
                | CHAR IDENTIFICADOR ASIGNAR CADENA PUNTOCOMA
                | FLOAT IDENTIFICADOR ASIGNAR NUMERO PUNTOCOMA

                | IDENTIFICADOR ASIGNAR NUMERO PUNTOCOMA
                | IDENTIFICADOR ASIGNAR CADENA PUNTOCOMA
                
                | INT IDENTIFICADOR ASIGNAR IDENTIFICADOR PUNTOCOMA
                | CHAR IDENTIFICADOR ASIGNAR IDENTIFICADOR PUNTOCOMA
                | FLOAT IDENTIFICADOR ASIGNAR IDENTIFICADOR PUNTOCOMA
                
    '''
#-----------------------------------------------------------------------------------------------------------------------     
#Condicional  if-else
def p_expresion_SI_SINO(t):
    '''
    if : SI PARIZQ condiciones_logicas PARDER
        | SI PARIZQ condiciones_logicas PARDER LLAIZQ instruccion LLADER
        | SI PARIZQ condiciones_logicas PARDER LLAIZQ instruccion LLADER SINO PARDER LLAIZQ instruccion LLADER
    '''
#-----------------------------------------------------------------------------------------------------------------------  
#Manejo de comentarios
def p_comentario_lienal(t):
    '''
    comentario_lineal : comments_ONELine  
    '''

def p_comentario_bloque(t):
    '''
    comentario_bloque : comments  
    '''
#-----------------------------------------------------------------------------------------------------------------------    
#Operaciones Logicas y Matematicas
def p_expresion_operaciones_math(t):
    '''
    operaciones_math : NUMERO SUMA NUMERO PUNTOCOMA
                |   NUMERO RESTA NUMERO PUNTOCOMA
                |   NUMERO MULT NUMERO PUNTOCOMA
                |   NUMERO DIV NUMERO PUNTOCOMA
                |   NUMERO POTENCIA NUMERO PUNTOCOMA
                |   NUMERO MODULO NUMERO PUNTOCOMA 

                |   NUMERO SUMA NUMERO operaciones_math
                |   NUMERO RESTA NUMERO operaciones_math
                |   NUMERO MULT NUMERO operaciones_math
                |   NUMERO DIV NUMERO operaciones_math
                |   NUMERO POTENCIA NUMERO operaciones_math
                |   NUMERO MODULO NUMERO operaciones_math

                |   SUMA NUMERO PUNTOCOMA
                |   RESTA NUMERO PUNTOCOMA
                |   MULT NUMERO PUNTOCOMA
                |   DIV NUMERO PUNTOCOMA
                |   POTENCIA NUMERO PUNTOCOMA
                |   MODULO NUMERO PUNTOCOMA
           
    '''
def p_operacion_booleana(t):
    '''
    operacion_booleana : expresion AND expresion 
                |  expresion OR expresion 
                |  expresion NOT expresion 
    '''
def p_condiciones_logicas(p):
    '''
    condiciones_logicas : IDENTIFICADOR RELATIONAL IDENTIFICADOR
            | NUMERO RELATIONAL NUMERO
            | IDENTIFICADOR RELATIONAL IDENTIFICADOR condiciones_logicas
            | IDENTIFICADOR LOGIC condiciones_logicas
            | BOOL 
            | BOOL LOGIC condiciones_logicas

    '''
#-----------------------------------------------------------------------------------------------------------------------  
#Ciclos
def p_expresion_mientras(t):
    '''
      while : MIENTRAS PARIZQ condiciones_logicas PARDER LLAIZQ instruccion LLADER 
    '''
def p_expresion_do(t):
    '''
      do : DO PARIZQ instruccion PARDER while 
    '''
#-----------------------------------------------------------------------------------------------------------------------  

def p_instruccion(t):
    '''
    instruccion : declaracion_asignar
                | if
                | comentario_lineal
                | comentario_bloque
                | operacion_booleana
                | condiciones_logicas
                | while
                | do
                | empty

    '''
def p_expresion_array(t):
    '''
    expresion  :   INT IDENTIFICADOR CORIZQ ENTERO CORDER ASIGNAR LLAIZQ ENTERO COMA ENTERO COMA ENTERO COMA ENTERO LLADER PUNTOCOMA

    '''

def p_expresion_include(t):
    '''
    expresion : NUMERAL INCLUDE MENORQUE expresion MAYORQUE

    '''

def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]


def p_expresion_cadena(t):
    'expresion : COMDOB expresion COMDOB'
    t[0] = t[2]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format(
            str(t.type), str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica


if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s:
            continue

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        prueba_sintactica(s)
