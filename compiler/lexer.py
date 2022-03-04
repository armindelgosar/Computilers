# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex

# list of token names
tokens = (
    'PLUS',
    'MINUS',
)

# Regular Expressions
t_PLUS = r'\+'
t_MINUS = r'-'

# Regular Expression rule with action

# Build the lexer
lexer = lex.lex()
