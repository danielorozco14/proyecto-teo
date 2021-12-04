import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'return': 'RETURN',
    'include': 'INCLUDE',
    'define': 'DEFINE',
}

tokens = [
    'NUMBER',
    'CHARACTER',
    'STRING',
    'ARITMETIC_OP_ADD',
    'ARITMETIC_OP_PROD',
    'RELATION_OP',
    'LOGIC_OP',
    'NEGATION',
    'BIT_OP',
    'LPAREN',
    'RPAREN',
    'BLOCK_START',
    'BLOCK_END',
    'ASSIGN',
    'COMMA',
    'EOI',
    'ID',
    'HASH'
] + list(reserved.values())
 
# Regular expression rules for simple tokens

def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_MULTICOMMENT(t):
    r'\/\*((.*(\n)*)*?)\*\/'
    pass

t_STRING = r'"(.*?)"'
t_CHARACTER = r'\'(\\\'|[^\']){1}\''
t_ARITMETIC_OP_ADD = r'(\+)|(\-)'
t_ARITMETIC_OP_PROD = r'(\*)|(\/)|(\%)'
t_NEGATION = r'(!(?!=))'
t_LOGIC_OP = r'(\|\|)|(\&\&)'
t_BIT_OP = r'(>>|<<|\&(?!\&)|\|(?!\|)|~|\^)'
t_RELATION_OP = r'(==)|(!=)|(>=)|(<=)|(<(?!<))|(>(?!>))'
t_LPAREN  = r'\('
t_RPAREN = r'\)'
t_BLOCK_START = r'\{'
t_BLOCK_END = r'\}'
t_ASSIGN = r'='
t_COMMA = r','
t_EOI = r';'
t_HASH = r'\#'
 
 # A regular expression rule with some action code
def t_NUMBER(t):
    r'(\d)+(\.(\d)+)?'

    if ("." in t.value):
        t.value = float(t.value)
    else:
        t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
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