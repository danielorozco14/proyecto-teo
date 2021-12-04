import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'GET',
    #-----------
    'CHAR',
    'INT',
    'FLOAT',
    'RETURN',
    'VOID',
    'ENDL',
    #'SI',
    #'SINO'
)
tokens = reservada +(
    'IDENTIFICADOR',
    'ENTERO',
    'FLOTANTE',
    'NUMERO',
    'CADENA',
    'OPERTACION_MATH',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',

    # Condiones
    'SI',
    'SINO',

    # Ciclos
    'MIENTRAS',
    'PARA',
    'DO',

    # logica
    'BOOL',
    'LOGIC',
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    'RELATIONAL',
    # Symbolos

    'NUMERAL',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',

    # Otros
    'comments_ONELine',
    'comments',
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER',  # >>
    'MAYORIZQ',  # <<,
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MINUSMINUS = r'\-\-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'\/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'\='
# Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'\<'
t_MAYORQUE = r'\>'
t_PUNTOCOMA = '\;'
t_COMA = r'\,'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_COMDOB = r'\"'
#-----------------------------------------------------------------------------------------------------------------------
#Tipos de Datos
def t_CHAR(t):
    r'char'
    return t

def t_INT(t):
    r'int'
    return t 

def t_FLOAT(t):
    r'float'
    return t
#-----------------------------------------------------------------------------------------------------------------------
#Utilización de variables
def t_IDENTIFICADOR(t):
    r'([a-z]|[A-Z]|_*([a-z]|[A-Z]))([a-z]|[A-Z]|\d|_)*'
    return t

#-----------------------------------------------------------------------------------------------------------------------
#Instrucciones: condicional if-else
def t_SI(t):
    r'if'
    return t

def t_SINO(t):
    r'else'
    return t
#-----------------------------------------------------------------------------------------------------------------------
#Declaración y definición de funciones
def t_VOID(t):
    r'void'
    return t
    
#-----------------------------------------------------------------------------------------------------------------------
#Manejo de comentarios 
def t_comments(t):
    r'\/\*(.|\n)*\*\/'
    pass

def t_comments_ONELine(t):
    r'\/\/.*'
    pass


#-----------------------------------------------------------------------------------------------------------------------
#Palabras claves o reservadas: return, using, namespace, std, cout, cin, get, endl
def t_RETURN(t):
    r'return'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_GET(t):
    r'get'
    return t

def t_ENDL(t):
    r'endl'
    return t

#-----------------------------------------------------------------------------------------------------------------------
#Cinco operadores aritméticos y cinco operados lógicos 
#Logicos
def t_LOGIC(t):
    r'(\&{2})|(\|{2})'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_RELATIONAL(t):
    r'(\>=)|(\<=)|(\==)|(\!=)|(\<)|(\>)'
    return t

def t_BOOL(t):
    r'(true)|(false)'
    return t
#-----------------------------------------------------------------------------------------------------------------------
#Directivas de inclusión y definición de macros 
def t_INCLUDE(t):
    r'include'
    return t

#-----------------------------------------------------------------------------------------------------------------------
#Instrucciones de iteración: do-while, while o for
def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_DO(t):
    r'do'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

#-----------------------------------------------------------------------------------------------------------------------
#Funciones para leer desde teclado y escribir en consola
def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

#-----------------------------------------------------------------------------------------------------------------------    
def t_NUMERO(t):
    r'(\d)+(\.(\d)+)?'
    if ("." in t.value):
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_FLOTANTE(t):
    r'(\d)+(\.(\d)+)?'
    if ("." in t.value):
        t.value = float(t.value)
        return t
        
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'(\"?(\w+ \ *\w*\d* \ *)\"?) |(\'?(\w+ \ *\w*\d* \ *)\'?)'
    return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                                    str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)
