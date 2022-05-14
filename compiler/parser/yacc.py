import ply.yacc as yacc
import logging
from compiler.lexer import tokens
from compiler.lexer import lexer
from compiler.statements import *
from compiler.parser import *

precedence = (
    ('right', 'ASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQ', 'NEQ'),
    ('nonassoc', 'LEQ', 'GEQ', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
    ('right', 'ELSE'),
    ('right', 'RPAREN'),
)

binary_operations = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div',
    '&&': 'and',
    '||': 'or',
    '==': 'eq',
    '!=': 'neq',
    '<': 'lt',
    '<=': 'leq',
    '>': 'gt',
    '>=': 'geq'
}


def make_parser(input_program):
    parser = yacc.yacc()
    logging.basicConfig(
        level=logging.CRITICAL,
    )
    log = logging.getLogger()
    result = parser.parse(input_program, lexer=lexer, debug=log)
    if parser.errorok:
        return True
    else:
        return False
