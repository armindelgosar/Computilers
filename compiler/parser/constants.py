from compiler.parser import p_empty


def p_constants(p):
    '''T_INTLITERAL
    | T_DOUBLELITERAL
    | T_BOOLEANLITERAL
    | T_STRINGLITERAL
    | NULL
    '''
    # semantic


def p_actual_expr(p):
    'ActualExpr : Expr | Expr COMMA ActualExpr'
    # semantic


def p_actuals(p):
    '''Actuals : ActualExpr
    | empty
    '''
    pass


def p_type(p):
    '''Type : INT
    | DOUBLE
    | BOOL
    | STRING
    | T_ID
    | Type LBRACKET RBRACKET
    '''
    pass
