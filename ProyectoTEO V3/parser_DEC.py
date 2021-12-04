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
    'HASH',
    'eof'
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
t_eof= r'\$'
 
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


# Analizador sintactico

# Auxiliares
while_stmt = 0       
statement = 1
compound_stmt = 2
local_instructions = 3
local_instructions_p = 4
local_instruction = 5
expression_stmt = 6
expression = 7
expression_p = 8
var_declaration = 9
var_declaration_p = 10
var_definition = 11
var_definition_p = 12
types = 13
condition = 14
condition_p = 15
condition_member = 16
simple_expression = 17
simple_expression_p = 18
additive_operation = 19
additive_operation_p = 20
prod_operation = 21
prod_operation_p = 22
factor = 23

# Tabla de parseo
tabla = [
    [while_stmt, 'WHILE', ['WHILE', 'LPAREN', condition, 'RPAREN', statement]],
    [while_stmt, 'LPAREN', None],
    [while_stmt, 'RPAREN', None],
    [while_stmt, 'BLOCK_START', None],
    [while_stmt, 'BLOCK_END', None],
    [while_stmt, 'EOI', None],
    [while_stmt, 'ID', None],
    [while_stmt, 'ASSIGN', None],
    [while_stmt, 'COMMA', None],
    [while_stmt, 'INT', None],
    [while_stmt, 'FLOAT', None],
    [while_stmt, 'CHAR', None],
    [while_stmt, 'NEGATION', None],
    [while_stmt, 'RELATION_OP', None],
    [while_stmt, 'ARITMETIC_OP_ADD', None],
    [while_stmt, 'ARITMETIC_OP_PROD', None],
    [while_stmt, 'LOGIC_OP', None],
    [while_stmt, 'NUMBER', None],
    [while_stmt, 'CHARACTER', None],
    [while_stmt, 'eof', None],

    [statement, 'WHILE', None],
    [statement, 'LPAREN', [expression_stmt]],
    [statement, 'RPAREN', None],
    [statement, 'BLOCK_START', [compound_stmt]],
    [statement, 'BLOCK_END', None],
    [statement, 'EOI', [expression_stmt]],
    [statement, 'ID', [expression_stmt]],
    [statement, 'ASSIGN', None],
    [statement, 'COMMA', None],
    [statement, 'INT', None],
    [statement, 'FLOAT', None],
    [statement, 'CHAR', None],
    [statement, 'NEGATION', None],
    [statement, 'RELATION_OP', None],
    [statement, 'ARITMETIC_OP_ADD', None],
    [statement, 'ARITMETIC_OP_PROD', None],
    [statement, 'LOGIC_OP', None],
    [statement, 'NUMBER', [expression_stmt]],
    [statement, 'CHARACTER', [expression_stmt]],
    [statement, 'eof', None],

    [compound_stmt, 'WHILE', None],
    [compound_stmt, 'LPAREN', None],
    [compound_stmt, 'RPAREN', None],
    [compound_stmt, 'BLOCK_START', ['BLOCK_START', local_instructions, 'BLOCK_END']],
    [compound_stmt, 'BLOCK_END', None],
    [compound_stmt, 'EOI', None],
    [compound_stmt, 'ID', None],
    [compound_stmt, 'ASSIGN', None],
    [compound_stmt, 'COMMA', None],
    [compound_stmt, 'INT', None],
    [compound_stmt, 'FLOAT', None],
    [compound_stmt, 'CHAR', None],
    [compound_stmt, 'NEGATION', None],
    [compound_stmt, 'RELATION_OP', None],
    [compound_stmt, 'ARITMETIC_OP_ADD', None],
    [compound_stmt, 'ARITMETIC_OP_PROD', None],
    [compound_stmt, 'LOGIC_OP', None],
    [compound_stmt, 'NUMBER', None],
    [compound_stmt, 'CHARACTER', None],
    [compound_stmt, 'eof', None],

    [local_instructions, 'WHILE', None],
    [local_instructions, 'LPAREN', [local_instructions_p]],
    [local_instructions, 'RPAREN', None],
    [local_instructions, 'BLOCK_START', [local_instructions_p]],
    [local_instructions, 'BLOCK_END', None],
    [local_instructions, 'EOI', None],
    [local_instructions, 'ID', [local_instructions_p]],
    [local_instructions, 'ASSIGN', None],
    [local_instructions, 'COMMA', None],
    [local_instructions, 'INT', [local_instructions_p]],
    [local_instructions, 'FLOAT', [local_instructions_p]],
    [local_instructions, 'CHAR', [local_instructions_p]],
    [local_instructions, 'NEGATION', None],
    [local_instructions, 'RELATION_OP', None],
    [local_instructions, 'ARITMETIC_OP_ADD', None],
    [local_instructions, 'ARITMETIC_OP_PROD', None],
    [local_instructions, 'LOGIC_OP', None],
    [local_instructions, 'NUMBER', [local_instructions_p]],
    [local_instructions, 'CHARACTER', [local_instructions_p]],
    [local_instructions, 'eof', None],

    [local_instructions_p, 'WHILE', None],
    [local_instructions_p, 'LPAREN', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'RPAREN', None],
    [local_instructions_p, 'BLOCK_START', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'BLOCK_END', ['empty']],
    [local_instructions_p, 'EOI', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'ID', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'ASSIGN', None],
    [local_instructions_p, 'COMMA', None],
    [local_instructions_p, 'INT', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'FLOAT', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'CHAR', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'NEGATION', None],
    [local_instructions_p, 'RELATION_OP', None],
    [local_instructions_p, 'ARITMETIC_OP_ADD', None],
    [local_instructions_p, 'ARITMETIC_OP_PROD', None],
    [local_instructions_p, 'LOGIC_OP', None],
    [local_instructions_p, 'NUMBER', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'CHARACTER', [local_instruction, local_instructions_p]],
    [local_instructions_p, 'eof', ['empty']],

    [local_instruction, 'WHILE', None],
    [local_instruction, 'LPAREN', [statement]],
    [local_instruction, 'RPAREN', None],
    [local_instruction, 'BLOCK_START', [statement]],
    [local_instruction, 'BLOCK_END', None],
    [local_instruction, 'EOI', [statement]],
    [local_instruction, 'ID', [statement]],
    [local_instruction, 'ASSIGN', None],
    [local_instruction, 'COMMA', None],
    [local_instruction, 'INT', [types, var_declaration, 'EOI']],
    [local_instruction, 'FLOAT', [types, var_declaration, 'EOI']],
    [local_instruction, 'CHAR', [types, var_declaration, 'EOI']],
    [local_instruction, 'NEGATION', None],
    [local_instruction, 'RELATION_OP', None],
    [local_instruction, 'ARITMETIC_OP_ADD', None],
    [local_instruction, 'ARITMETIC_OP_PROD', None],
    [local_instruction, 'LOGIC_OP', None],
    [local_instruction, 'NUMBER', [statement]],
    [local_instruction, 'CHARACTER', [statement]],
    [local_instruction, 'eof', None],

    [expression_stmt, 'WHILE', None],
    [expression_stmt, 'LPAREN', [expression, 'EOI']],
    [expression_stmt, 'RPAREN', None],
    [expression_stmt, 'BLOCK_START', None],
    [expression_stmt, 'BLOCK_END', None],
    [expression_stmt, 'EOI', ['EOI']],
    [expression_stmt, 'ID', [expression, 'EOI']],
    [expression_stmt, 'ASSIGN', None],
    [expression_stmt, 'COMMA', None],
    [expression_stmt, 'INT', None],
    [expression_stmt, 'FLOAT', None],
    [expression_stmt, 'CHAR', None],
    [expression_stmt, 'NEGATION', None],
    [expression_stmt, 'RELATION_OP', None],
    [expression_stmt, 'ARITMETIC_OP_ADD', None],
    [expression_stmt, 'ARITMETIC_OP_PROD', None],
    [expression_stmt, 'LOGIC_OP', None],
    [expression_stmt, 'NUMBER', [expression, 'EOI']],
    [expression_stmt, 'CHARACTER', [expression, 'EOI']],
    [expression_stmt, 'eof', None],

    [expression, 'WHILE', None],
    [expression, 'LPAREN', [expression_p, simple_expression]],
    [expression, 'RPAREN', None],
    [expression, 'BLOCK_START', None],
    [expression, 'BLOCK_END', None],
    [expression, 'EOI', None],
    [expression, 'ID', [expression_p, simple_expression]],
    [expression, 'ASSIGN', None],
    [expression, 'COMMA', None],
    [expression, 'INT', None],
    [expression, 'FLOAT', None],
    [expression, 'CHAR', None],
    [expression, 'NEGATION', None],
    [expression, 'RELATION_OP', None],
    [expression, 'ARITMETIC_OP_ADD', None],
    [expression, 'ARITMETIC_OP_PROD', None],
    [expression, 'LOGIC_OP', None],
    [expression, 'NUMBER', [expression_p, simple_expression]],
    [expression, 'CHARACTER', [expression_p, simple_expression]],
    [expression, 'eof', None],

    [expression_p, 'WHILE', None],
    [expression_p, 'LPAREN', ['empty']],
    [expression_p, 'RPAREN', None],
    [expression_p, 'BLOCK_START', None],
    [expression_p, 'BLOCK_END', None],
    [expression_p, 'EOI', None],
    [expression_p, 'ID', ['ID', 'ASSIGN']],
    [expression_p, 'ASSIGN', None],
    [expression_p, 'COMMA', None],
    [expression_p, 'INT', None],
    [expression_p, 'FLOAT', None],
    [expression_p, 'CHAR', None],
    [expression_p, 'NEGATION', None],
    [expression_p, 'RELATION_OP', None],
    [expression_p, 'ARITMETIC_OP_ADD', None],
    [expression_p, 'ARITMETIC_OP_PROD', None],
    [expression_p, 'LOGIC_OP', None],
    [expression_p, 'NUMBER', ['empty']],
    [expression_p, 'CHARACTER', ['empty']],
    [expression_p, 'eof', ['empty']],

    [var_declaration, 'WHILE', None],
    [var_declaration, 'LPAREN', None],
    [var_declaration, 'RPAREN', None],
    [var_declaration, 'BLOCK_START', None],
    [var_declaration, 'BLOCK_END', None],
    [var_declaration, 'EOI', None],
    [var_declaration, 'ID', [var_definition, var_declaration_p]],
    [var_declaration, 'ASSIGN', None],
    [var_declaration, 'COMMA', None],
    [var_declaration, 'INT', None],
    [var_declaration, 'FLOAT', None],
    [var_declaration, 'CHAR', None],
    [var_declaration, 'NEGATION', None],
    [var_declaration, 'RELATION_OP', None],
    [var_declaration, 'ARITMETIC_OP_ADD', None],
    [var_declaration, 'ARITMETIC_OP_PROD', None],
    [var_declaration, 'LOGIC_OP', None],
    [var_declaration, 'NUMBER', None],
    [var_declaration, 'CHARACTER', None],
    [var_declaration, 'eof', None],

    [var_declaration_p, 'WHILE', None],
    [var_declaration_p, 'LPAREN', None],
    [var_declaration_p, 'RPAREN', None],
    [var_declaration_p, 'BLOCK_START', None],
    [var_declaration_p, 'BLOCK_END', None],
    [var_declaration_p, 'EOI', ['empty']],
    [var_declaration_p, 'ID', None],
    [var_declaration_p, 'ASSIGN', None],
    [var_declaration_p, 'COMMA', ['COMMA', var_definition, var_declaration_p]],
    [var_declaration_p, 'INT', None],
    [var_declaration_p, 'FLOAT', None],
    [var_declaration_p, 'CHAR', None],
    [var_declaration_p, 'NEGATION', None],
    [var_declaration_p, 'RELATION_OP', None],
    [var_declaration_p, 'ARITMETIC_OP_ADD', None],
    [var_declaration_p, 'ARITMETIC_OP_PROD', None],
    [var_declaration_p, 'LOGIC_OP', None],
    [var_declaration_p, 'NUMBER', None],
    [var_declaration_p, 'CHARACTER', None],
    [var_declaration_p, 'eof', ['empty']],

    [var_definition, 'WHILE', None],
    [var_definition, 'LPAREN', None],
    [var_definition, 'RPAREN', None],
    [var_definition, 'BLOCK_START', None],
    [var_definition, 'BLOCK_END', None],
    [var_definition, 'EOI', None],
    [var_definition, 'ID', ['ID', var_definition_p]],
    [var_definition, 'ASSIGN', None],
    [var_definition, 'COMMA', None],
    [var_definition, 'INT', None],
    [var_definition, 'FLOAT', None],
    [var_definition, 'CHAR', None],
    [var_definition, 'NEGATION', None],
    [var_definition, 'RELATION_OP', None],
    [var_definition, 'ARITMETIC_OP_ADD', None],
    [var_definition, 'ARITMETIC_OP_PROD', None],
    [var_definition, 'LOGIC_OP', None],
    [var_definition, 'NUMBER', None],
    [var_definition, 'CHARACTER', None],
    [var_definition, 'eof', None],

    [var_definition_p, 'WHILE', None],
    [var_definition_p, 'LPAREN', None],
    [var_definition_p, 'RPAREN', None],
    [var_definition_p, 'BLOCK_START', None],
    [var_definition_p, 'BLOCK_END', None],
    [var_definition_p, 'EOI', ['empty']],
    [var_definition_p, 'ID', None],
    [var_definition_p, 'ASSIGN', ['ASSIGN', simple_expression]],
    [var_definition_p, 'COMMA', ['empty']],
    [var_definition_p, 'INT', None],
    [var_definition_p, 'FLOAT', None],
    [var_definition_p, 'CHAR', None],
    [var_definition_p, 'NEGATION', None],
    [var_definition_p, 'RELATION_OP', None],
    [var_definition_p, 'ARITMETIC_OP_ADD', None],
    [var_definition_p, 'ARITMETIC_OP_PROD', None],
    [var_definition_p, 'LOGIC_OP', None],
    [var_definition_p, 'NUMBER', None],
    [var_definition_p, 'CHARACTER', None],
    [var_definition_p, 'eof', ['empty']],

    [types, 'WHILE', None],
    [types, 'LPAREN', None],
    [types, 'RPAREN', None],
    [types, 'BLOCK_START', None],
    [types, 'BLOCK_END', None],
    [types, 'EOI', None],
    [types, 'ID', None],
    [types, 'ASSIGN', None],
    [types, 'COMMA', None],
    [types, 'INT', ['INT']],
    [types, 'FLOAT', ['FLOAT']],
    [types, 'CHAR', ['CHAR']],
    [types, 'NEGATION', None],
    [types, 'RELATION_OP', None],
    [types, 'ARITMETIC_OP_ADD', None],
    [types, 'ARITMETIC_OP_PROD', None],
    [types, 'LOGIC_OP', None],
    [types, 'NUMBER', None],
    [types, 'CHARACTER', None],
    [types, 'eof', None],

    [condition, 'WHILE', None],
    [condition, 'LPAREN', [condition_member, condition_p]],
    [condition, 'RPAREN', None],
    [condition, 'BLOCK_START', None],
    [condition, 'BLOCK_END', None],
    [condition, 'EOI', None],
    [condition, 'ID', [condition_member, condition_p]],
    [condition, 'ASSIGN', None],
    [condition, 'COMMA', None],
    [condition, 'INT', None],
    [condition, 'FLOAT', None],
    [condition, 'CHAR', None],
    [condition, 'NEGATION', [condition_member, condition_p]],
    [condition, 'RELATION_OP', None],
    [condition, 'ARITMETIC_OP_ADD', None],
    [condition, 'ARITMETIC_OP_PROD', None],
    [condition, 'LOGIC_OP', None],
    [condition, 'NUMBER', [condition_member, condition_p]],
    [condition, 'CHARACTER', [condition_member, condition_p]],
    [condition, 'eof', None],

    [condition_p, 'WHILE', None],
    [condition_p, 'LPAREN', None],
    [condition_p, 'RPAREN', ['empty']],
    [condition_p, 'BLOCK_START', None],
    [condition_p, 'BLOCK_END', None],
    [condition_p, 'EOI', None],
    [condition_p, 'ID', None],
    [condition_p, 'ASSIGN', None],
    [condition_p, 'COMMA', None],
    [condition_p, 'INT', None],
    [condition_p, 'FLOAT', None],
    [condition_p, 'CHAR', None],
    [condition_p, 'NEGATION', None],
    [condition_p, 'RELATION_OP', None],
    [condition_p, 'ARITMETIC_OP_ADD', None],
    [condition_p, 'ARITMETIC_OP_PROD', None],
    [condition_p, 'LOGIC_OP', ['LOGIC_OP', condition_member, condition_p]],
    [condition_p, 'NUMBER', None],
    [condition_p, 'CHARACTER', None],
    [condition_p, 'eof', ['empty']],

    [condition_member, 'WHILE', None],
    [condition_member, 'LPAREN', [simple_expression]],
    [condition_member, 'RPAREN', None],
    [condition_member, 'BLOCK_START', None],
    [condition_member, 'BLOCK_END', None],
    [condition_member, 'EOI', None],
    [condition_member, 'ID', [simple_expression]],
    [condition_member, 'ASSIGN', None],
    [condition_member, 'COMMA', None],
    [condition_member, 'INT', None],
    [condition_member, 'FLOAT', None],
    [condition_member, 'CHAR', None],
    [condition_member, 'NEGATION', ['NEGATION', simple_expression]],
    [condition_member, 'RELATION_OP', None],
    [condition_member, 'ARITMETIC_OP_ADD', None],
    [condition_member, 'ARITMETIC_OP_PROD', None],
    [condition_member, 'LOGIC_OP', None],
    [condition_member, 'NUMBER', [simple_expression]],
    [condition_member, 'CHARACTER', [simple_expression]],
    [condition_member, 'eof', None],
    
    [simple_expression, 'WHILE', None],
    [simple_expression, 'LPAREN', [additive_operation, simple_expression_p]],
    [simple_expression, 'RPAREN', None],
    [simple_expression, 'BLOCK_START', None],
    [simple_expression, 'BLOCK_END', None],
    [simple_expression, 'EOI', None],
    [simple_expression, 'ID', [additive_operation, simple_expression_p]],
    [simple_expression, 'ASSIGN', None],
    [simple_expression, 'COMMA', None],
    [simple_expression, 'INT', None],
    [simple_expression, 'FLOAT', None],
    [simple_expression, 'CHAR', None],
    [simple_expression, 'NEGATION', None],
    [simple_expression, 'RELATION_OP', None],
    [simple_expression, 'ARITMETIC_OP_ADD', None],
    [simple_expression, 'ARITMETIC_OP_PROD', None],
    [simple_expression, 'LOGIC_OP', None],
    [simple_expression, 'NUMBER', [additive_operation, simple_expression_p]],
    [simple_expression, 'CHARACTER', [additive_operation, simple_expression_p]],
    [simple_expression, 'eof', None],

    [simple_expression_p, 'WHILE', None],
    [simple_expression_p, 'LPAREN', None],
    [simple_expression_p, 'RPAREN', ['empty']],
    [simple_expression_p, 'BLOCK_START', None],
    [simple_expression_p, 'BLOCK_END', None],
    [simple_expression_p, 'EOI', ['empty']],
    [simple_expression_p, 'ID', None],
    [simple_expression_p, 'ASSIGN', None],
    [simple_expression_p, 'COMMA', ['empty']],
    [simple_expression_p, 'INT', None],
    [simple_expression_p, 'FLOAT', None],
    [simple_expression_p, 'CHAR', None],
    [simple_expression_p, 'NEGATION', None],
    [simple_expression_p, 'RELATION_OP', ['RELATION_OP', additive_operation, simple_expression_p]],
    [simple_expression_p, 'ARITMETIC_OP_ADD', None],
    [simple_expression_p, 'ARITMETIC_OP_PROD', None],
    [simple_expression_p, 'LOGIC_OP', ['empty']],
    [simple_expression_p, 'NUMBER', None],
    [simple_expression_p, 'CHARACTER', None],
    [simple_expression_p, 'eof', ['empty']],

    [additive_operation, 'WHILE', None],
    [additive_operation, 'LPAREN', [prod_operation, additive_operation_p]],
    [additive_operation, 'RPAREN', None],
    [additive_operation, 'BLOCK_START', None],
    [additive_operation, 'BLOCK_END', None],
    [additive_operation, 'EOI', None],
    [additive_operation, 'ID', [prod_operation, additive_operation_p]],
    [additive_operation, 'ASSIGN', None],
    [additive_operation, 'COMMA', None],
    [additive_operation, 'INT', None],
    [additive_operation, 'FLOAT', None],
    [additive_operation, 'CHAR', None],
    [additive_operation, 'NEGATION', None],
    [additive_operation, 'RELATION_OP', None],
    [additive_operation, 'ARITMETIC_OP_ADD', None],
    [additive_operation, 'ARITMETIC_OP_PROD', None],
    [additive_operation, 'LOGIC_OP', None],
    [additive_operation, 'NUMBER', [prod_operation, additive_operation_p]],
    [additive_operation, 'CHARACTER', [prod_operation, additive_operation_p]],
    [additive_operation, 'eof', None],

    [additive_operation_p, 'WHILE', None],
    [additive_operation_p, 'LPAREN', None],
    [additive_operation_p, 'RPAREN', ['empty']],
    [additive_operation_p, 'BLOCK_START', None],
    [additive_operation_p, 'BLOCK_END', None],
    [additive_operation_p, 'EOI', ['empty']],
    [additive_operation_p, 'ID', None],
    [additive_operation_p, 'ASSIGN', None],
    [additive_operation_p, 'COMMA', ['empty']],
    [additive_operation_p, 'INT', None],
    [additive_operation_p, 'FLOAT', None],
    [additive_operation_p, 'CHAR', None],
    [additive_operation_p, 'NEGATION', None],
    [additive_operation_p, 'RELATION_OP', ['empty']],
    [additive_operation_p, 'ARITMETIC_OP_ADD', ['ARITMETIC_OP_ADD', prod_operation, additive_operation_p]],
    [additive_operation_p, 'ARITMETIC_OP_PROD', None],
    [additive_operation_p, 'LOGIC_OP', ['empty']],
    [additive_operation_p, 'NUMBER', None],
    [additive_operation_p, 'CHARACTER', None],
    [additive_operation_p, 'eof', ['empty']],

    [prod_operation, 'WHILE', None],
    [prod_operation, 'LPAREN', [factor, prod_operation_p]],
    [prod_operation, 'RPAREN', None],
    [prod_operation, 'BLOCK_START', None],
    [prod_operation, 'BLOCK_END', None],
    [prod_operation, 'EOI', None],
    [prod_operation, 'ID', [factor, prod_operation_p]],
    [prod_operation, 'ASSIGN', None],
    [prod_operation, 'COMMA', None],
    [prod_operation, 'INT', None],
    [prod_operation, 'FLOAT', None],
    [prod_operation, 'CHAR', None],
    [prod_operation, 'NEGATION', None],
    [prod_operation, 'RELATION_OP', None],
    [prod_operation, 'ARITMETIC_OP_ADD', None],
    [prod_operation, 'ARITMETIC_OP_PROD', None],
    [prod_operation, 'LOGIC_OP', None],
    [prod_operation, 'NUMBER', [factor, prod_operation_p]],
    [prod_operation, 'CHARACTER', [factor, prod_operation_p]],
    [prod_operation, 'eof', None],

    [prod_operation_p, 'WHILE', None],
    [prod_operation_p, 'LPAREN', None],
    [prod_operation_p, 'RPAREN', ['empty']],
    [prod_operation_p, 'BLOCK_START', None],
    [prod_operation_p, 'BLOCK_END', None],
    [prod_operation_p, 'EOI', ['empty']],
    [prod_operation_p, 'ID', None],
    [prod_operation_p, 'ASSIGN', None],
    [prod_operation_p, 'COMMA', ['empty']],
    [prod_operation_p, 'INT', None],
    [prod_operation_p, 'FLOAT', None],
    [prod_operation_p, 'CHAR', None],
    [prod_operation_p, 'NEGATION', None],
    [prod_operation_p, 'RELATION_OP', ['empty']],
    [prod_operation_p, 'ARITMETIC_OP_ADD', ['empty']],
    [prod_operation_p, 'ARITMETIC_OP_PROD', ['ARITMETIC_OP_PROD', factor, prod_operation_p]],
    [prod_operation_p, 'LOGIC_OP', ['empty']],
    [prod_operation_p, 'NUMBER', None],
    [prod_operation_p, 'CHARACTER', None],
    [prod_operation_p, 'eof', ['empty']],

    [factor, 'WHILE', None],
    [factor, 'LPAREN', ['LPAREN', simple_expression, 'RPAREN']],
    [factor, 'RPAREN', None],
    [factor, 'BLOCK_START', None],
    [factor, 'BLOCK_END', None],
    [factor, 'EOI', None],
    [factor, 'ID', ['ID']],
    [factor, 'ASSIGN', None],
    [factor, 'COMMA', None],
    [factor, 'INT', None],
    [factor, 'FLOAT', None],
    [factor, 'CHAR', None],
    [factor, 'NEGATION', None],
    [factor, 'RELATION_OP', None],
    [factor, 'ARITMETIC_OP_ADD', None],
    [factor, 'ARITMETIC_OP_PROD', None],
    [factor, 'LOGIC_OP', None],
    [factor, 'NUMBER', ['NUMBER']],
    [factor, 'CHARACTER', ['CHARACTER']],
    [factor, 'eof', None],
]

stack = ['eof', 0]

def miParser(code):
    f = open('c.c', 'r')
    code = f.read()
    #lexer.input(f.read())
    lexer.input(code)
    
    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    while True:    
        if x == tok.type and x == 'eof':
            print("Cadena reconocida exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x=stack[-1]
                tok=lexer.token()                
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                return 0;
            if x not in tokens: #es no terminal
                print("van entrar a la tabla:")
                print(x)
                print(tok.type)
                celda=buscar_en_tabla(x,tok.type)                            
                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print("En posición:", tok.lexpos)
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("------------")
                    x=stack[-1]            

            
        #if not tok:
            #break
        #print(tok)
        #print(tok.type, tok.value, tok.lineno, tok.lexpos)

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
        i = input('filename >')
        f = open(i, 'r')
        code = f.read()

        miParser(code)
    except IOError:
        print("File not found")


main()