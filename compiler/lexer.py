import ply.lex as lex

reserved = {
    '__func__': 'FUNC',
    '__line__': 'LINE',
    'bool': 'BOOL',
    'break': 'BREAK',
    'btoi': 'BTOI',
    'class': 'CLASS',
    'continue': 'CONTINUE',
    'define': 'DEFINE',
    'double': 'DOUBLE',
    'dtoi': 'DTOI',
    'else': 'ELSE',
    'for': 'FOR',
    'if': 'IF',
    'import': 'IMPORT',
    'int': 'INT',
    'itob': 'ITOB',
    'itod': 'ITOD',
    'new': 'NEW',
    'NewArray': 'NEWARRAY',
    'null': 'NULL',
    'Print': 'PRINT',
    'private': 'PRIVATE',
    'public': 'PUBLIC',
    'ReadInteger': 'READINTEGER',
    'ReadLine': 'READLINE',
    'return': 'RETURN',
    'string': 'STRING',
    'this': 'THIS',
    'void': 'VOID',
    'while': 'WHILE',
}
tokens = [
             'T_INTLITERAL',
             'T_DOUBLELITERAL',
             'T_STRINGLITERAL',
             'T_BOOLEANLITERAL',
             'T_ID',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'LBRACE',
             'RBRACE',
             'LBRACKET',
             'RBRACKET',
             'SEMICOLON',
             'BAR',
             'EQUAL',
             'LOGICAL_OR',
             'LOGICAL_AND',
             'LOGICAL_EQUAL',
             'LOGICAL_NON_EQUAL',
             'BIGGER_THAN',
             'BIGGER_THAN_OR_EQUAL',
             'SMALLER_THAN',
             'SMALLER_THAN_OR_EQUAL',
             'COMMA',
             'ignore',
             'newline',
             'error',
         ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r'\;'
t_BAR = r'\|'
t_EQUAL = r'\='
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_AND = r'\&\&'
t_LOGICAL_EQUAL = r'\=\='
t_LOGICAL_NON_EQUAL = r'\!\='
t_BIGGER_THAN = r'\>'
t_BIGGER_THAN_OR_EQUAL = r'\>\='
t_SMALLER_THAN = r'\<'
t_SMALLER_THAN_OR_EQUAL = r'\<\='
t_COMMA = r'\,'
t_ignore = ' \t'
# reserved Regular Expressions
t_FUNC = r'__func__'
t_LINE = r'__line__'
t_BOOL = r'bool'
t_BREAK = r'break'
t_BTOI = r'btoi'
t_CLASS = r'class'
t_CONTINUE = r'continue'
t_DEFINE = r'define'
t_DOUBLE = r'double'
t_DTOI = r'dtoi'
t_ELSE = r'else'
t_FOR = r'for'
t_IF = r'if'
t_IMPORT = r'import'
t_INT = r'int'
t_ITOB = r'itob'
t_ITOD = r'ITOD'
t_NEW = r'new'
t_NEWARRAY = r'NewArray'
t_NULL = r'null'
t_PRINT = r'Print'
t_PRIVATE = r'private'
t_PUBLIC = r'public'
t_READINTEGER = r'ReadInteger'
t_READLINE = r'ReadLine'
t_RETURN = r'return'
t_STRING = r'string'
t_THIS = r'this'
t_VOID = r'void'
t_WHILE = r'while'


t_T_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_T_DOUBLELITERAL = r'/^[0-9]+(\\.[0-9]+)?$'
t_T_STRINGLITERAL = r'"(?s).+"'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_T_INTLITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_T_BOOLEANLITERAL(t):
    r'(?<![a-zA-Z0-9_])(true|false)(?![a-zA-Z0-9_])'
    t.type = reserved.get(t.value, 'T_BOOLEANLITERAL')
    return t


def t_error(t):
    print("UNDEFINED_TOKEN")
    t.lexer.skip(1)


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reserved.get(t.value, 'T_ID')  # Check for reserved words
    return t


lexer = lex.lex()
