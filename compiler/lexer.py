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
    'PLUS',
    'MINUS',
)

# Regular Expressions
# here is the regex patterns which should we define for every token and should start with 't_'
t_PLUS = r'\+'
t_MINUS = r'-'

# Regular Expression rule with action
# here is for action methods (for example setting value of lexeme for an integer)

# Build the lexer
lexer = lex.lex()
