def p_continue_stmt(p):
    'ContinueStmt : CONTINUE SEMICOLON'
    # p[0] = ContinueStmt(p[1])


def p_break_stmt(p):
    'BreakStmt : BREAK SEMICOLON'
    # add semantic


def p_if_stmt(p):
    '''IfStmt : IF LPAREN Expr RPAREN Stmt
    | IF LPAREN Expr RPAREN Stmt ELSE Stmt
    '''
    # Semantic definition


def p_while_stmt(p):
    'WhileStmt : WHILE LPAREN Expr RPAREN Stmt'
    # Semantic definition
