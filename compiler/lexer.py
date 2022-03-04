import ply.lex as lex


tokens = (
    'T_INTLITERAL',
    'T_DOUBLELITERAL',
    'T_STRINGLITERAL',
    'T_BOOLEANLITERAL',
    'T_ID',
    'DEFINE',
    'IMPORT',
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
)

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
t_T_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_T_DOUBLELITERAL = r'/^[0-9]+(\\.[0-9]+)?$'
t_T_STRINGLITERAL = r'"(?s).+"'
# t_T_INTLITERAL = r'\d+'
t_T_BOOLEANLITERAL = r'^(?i)(true|false)$'
t_DEFINE = r'define'
t_IMPORT = r'import'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_T_INTLITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("UNDEFINED_TOKEN")
    t.lexer.skip(1)


lexer = lex.lex()
