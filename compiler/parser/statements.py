def p_if_stmt(p):
    '''IfStmt : IF LPAREN Expr RPAREN Stmt
    | IF LPAREN Expr RPAREN Stmt ELSE Stmt
    '''
    # Semantic definition


def p_while_stmt(p):
    'WhileStmt : WHILE LPAREN Expr RPAREN Stmt'
    # Semantic definition


def p_for_stmt(p):
    '''ForStmt : FOR LPAREN Expr SEMICOLON Expr SEMICOLON Expr RPAREN Stmt
    | FOR LPAREN SEMICOLON Expr SEMICOLON Expr RPAREN Stmt
    | FOR LPAREN Expr SEMICOLON Expr SEMICOLON RPAREN Stmt
    FOR LPAREN SEMICOLON Expr SEMICOLON RPAREN Stmt
    '''
    # semantic definition


def p_return_stmt(p):
    'ReturnStmt: RETURN SEMICOLON | RETURN Expr SEMICOLON'
    # semantic definition


def p_break_stmt(p):
    'BreakStmt : BREAK SEMICOLON'
    # add semantic


def p_continue_stmt(p):
    'ContinueStmt : CONTINUE SEMICOLON'
    # p[0] = ContinueStmt(p[1])
