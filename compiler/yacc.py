import ply.yacc as yacc
import logging
from lexer import tokens
from compiler.lexer import lexer


def p_constant(p):
    '''Constant : intConstant
    | doubleConstant
    | boolConstant
    | stringConstant
    | null'''
    p[0] = p[1]


def p_call(p):
    '''Call : ident (Actuals)
    | Expr . ident (Actuals)'''


def p_boolconstant(p):
    '''boolConstant : T_BOOLEANLITERAL
    '''
    p[0] = p[1]


def p_error(p):
    if p is None:
        print("unexpected end of file")
    else:
        print("unexpected token : " + str(p))


def make_parser(input_program):
    parser = yacc.yacc()
    logging.basicConfig(
        level=logging.CRITICAL,
    )
    log = logging.getLogger()
    result = parser.parse(input_program, lexer=lexer, debug=log)
    if parser.errorok:
        print("Parsing succeeded")
    else:
        print("Parsing failed")
