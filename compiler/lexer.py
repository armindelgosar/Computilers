# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex

# list of token names
# each token pattern which you want to add should be added to this tuple before all.
tokens = (
    'T_INTLITERAL',
    'T_DOUBLELITERAL',
    'T_STRINGLITERAL',
    'T_BOOLEANLITERAL',
    'T_ID',
    'PLUS ',
    'MINUS',
    'TIMES',
    'DIVID',
    'LPARE',
    'RPARE',
    'ignore',
)

# Regular Expressions
# here is the regex patterns which should we define for every token and should start with 't_'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'
t_T_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_T_DOUBLELITERAL = r'/^[0-9]+(\\.[0-9]+)?$'
t_T_STRINGLITERAL = r'(?s).*'
t_T_INTLITERAL = r'^\d+$'
t_T_BOOLEANLITERAL = r'^(?i)(true|false)$'


# Regular Expression rule with action
# here is for action methods (for example setting value of lexeme for an integer)

def t_T_INTLITERAL(t):
    t.value = int(t.value)
    return t


def t_T_DOUBLELITERAL(t):
    t.value = float(t.value)
    return t


def t_T_STRINGLITERAL(t):
    t.value = str(t.value)
    return t


def t_T_BOOLEANLITERAL(t):
    t.value = bool(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)


# Error handling rule
def t_error(t):
    print("UNDEFINED_TOKEN")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
