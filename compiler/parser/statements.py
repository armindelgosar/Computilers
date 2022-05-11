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


def p_variable_decl(p):
    'VariableDecl: Variable SEMICOLON'


def p_variable(p):
    'Variable : Type T_ID'


def p_type(p):
    '''Type: INT
    | DOUBLE
    | T_ID
    | BOOL
    | STRING
    | Type LBRACE RBRACE
    '''


def p_program(p):
    'Program : ProgramMacroExpr ProgramDeclExpr'


def p_program_macro_expr(p):
    '''ProgramMacroExpr : ProgramMacroExpr Macro
    | empty
    '''


def p_program_decl_expr(p):
    '''ProgramDeclExpr : Decl
    | ProgramDeclExpr Decl
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


def p_function_decl(p):
    """
    FunctionDecl : Type T_ID LPAREN Formals RPAREN StmtBlock
    | VOID T_ID LPAREN Formals RPAREN StmtBlock
    """


def p_class_decl(p):
    """
    ClassDecl : CLASS T_ID SMALLER_THAN EXTENDS T_id BIGGER_THAN SMALLER_THAN IMPLEMENTS TIDEXPR BIGGER_THAN LBRACE FieldExpr RBRACE
    | VOID T_ID LPAREN Formals RPAREN StmtBlock
    """


def p_tid_expr(p):
    """
    TIDEXPR: T_ID
    | TIDEXPR COMMA T_ID
    """


def p_field_expr(p):
    """
    FieldExpr : FieldExpr Field
    | empty
    """


def p_variable_expr(p):
    """
    VariableExpr : Variable
    | VariableExpr COMMA Variable
    """


def p_formals(p):
    """
    Formals : VariableExpr
    | empty
    """


def p_field(p):
    """
    Field : AccessMode  VariableDecl
    | AccessMode  FunctionDecl
    """


def p_access_mode(p):
    """
    AccessMode: PRIVATE
    | PROTECTED
    | PUBLIC
    | empty
    """


def p_interface_decl(p):
    """
    InterfaceDecl : INTERFACE T_id LBRACE PrototypeExpr RBRACE
    """


def p_prototype(p):
    """
    ProtoType : Type T_id LPAREN Formals RPAREN SEMICOLON
    | VOID T_id LPAREN Formals RPAREN SEMICOLON
    """


def p_prototype_expr(p):
    """
    PrototypeExpr : PrototypeExpr ProtoType
    | empty
    """
