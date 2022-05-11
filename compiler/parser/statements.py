def p_prototype(p):
    '''Prototype : Type T_ID LPAREN Formals RPAREN SEMICOLON
    | VOID T_ID LPAREN Formals RPAREN SEMICOLON
    '''

def p_macro(p):
    'Macro : IMPORT STRING'

def p_decl(p):
    '''Decl : VariableDecl
    | FunctionDecl
    | ClassDecl
    | InterfaceDecl
    '''


def p_program(p):
    'Program : ProgramMacroExpr ProgramDeclExpr'


def p_program_macro_expr(p):
    '''ProgramMacroExpr : Macro
    | empty
    '''

def p_program_decl_expr(p):
    '''ProgramDeclExpr : Decl
    | ProgramDeclExprDecl
    '''



def p_stmt(p):
    '''Expr SEMICOLON
    | SEMICOLON
    | IfStmt
    | WhileStmt
    | ForStmt
    | BreakStmt
    | ContinueStmt
    | ReturnStmt
    | PrintStmt
    | StmtBlock
    '''
    # semantics


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


def p_print_expr(p):
    '''PrintExpr : Expr
    | Expr COMMA PrintExpr
    '''
    # semantic


def p_print_stmt(p):
    'PrintStmt : Print LPAREN PrintExpr RPAREN SEMICOLON'
    # semantic
