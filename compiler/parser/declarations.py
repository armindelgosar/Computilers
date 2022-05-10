def p_variable(p):
    'Variable : Type T_ID'
    pass


def p_variable_decl(p):
    'VariableDecl : Variable SEMICOLON'
    pass


def p_function_decl(p):
    '''FunctionDecl : Type T_ID LPAREN Formals RPAREN StmtBlock
    | VOID T_ID LPAREN Formals RPAREN StmtBlock
    '''
    pass


def p_variable_extra(p):
    '''VariableExtra : Variable
    | Variable COMMA VariableExtra
    '''
    pass


def p_formals(p):
    '''Formals : empty
    | VariableExtra
    '''
    pass
