import ply.yacc as yacc
from compiler.lexer import *


def p_actual_expr(p):
    '''ActualExpr : Expr
    | Expr COMMA ActualExpr'''
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


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p is None:
        print("unexpected end of file")
    else:
        print("unexpected token : " + str(p))


def p_macro(p):
    'Macro : IMPORT T_STRINGLITERAL'


def p_decl(p):
    '''Decl : VariableDecl
    | FunctionDecl
    | ClassDecl
    | InterfaceDecl
    '''


def p_variable_decl_expr(p):
    """
    VariableDeclExpr : VariableDeclExpr VariableDecl
    | empty
    """


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
    '''Stmt : SMALLER_THAN Expr BIGGER_THAN SEMICOLON
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


def p_stmt_expr(p):
    """
    StmtExpr : StmtExpr Stmt
    | empty
    """


def p_stmt_block(p):
    """
    StmtBlock : LBRACE VariableDeclExpr StmtExpr RBRACE
    | empty
    """


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
    | FOR LPAREN SEMICOLON Expr SEMICOLON RPAREN Stmt
    '''
    # semantic definition


def p_return_stmt(p):
    '''ReturnStmt : RETURN SEMICOLON
    | RETURN Expr SEMICOLON'''
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
    'PrintStmt : PRINT LPAREN PrintExpr RPAREN SEMICOLON'
    # semantic


def p_class_decl(p):
    """
    ClassDecl : CLASS T_ID SMALLER_THAN EXTENDS T_ID BIGGER_THAN SMALLER_THAN IMPLEMENTS TIDEXPR BIGGER_THAN LBRACE FieldExpr RBRACE
    | VOID T_ID LPAREN Formals RPAREN StmtBlock
    """


def p_tid_expr(p):
    """
    TIDEXPR : T_ID
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
    AccessMode : PRIVATE
    | PROTECTED
    | PUBLIC
    | empty
    """


def p_interface_decl(p):
    """
    InterfaceDecl : INTERFACE T_ID LBRACE PrototypeExpr RBRACE
    """


def p_prototype(p):
    """
    ProtoType : Type T_ID LPAREN Formals RPAREN SEMICOLON
    | VOID T_ID LPAREN Formals RPAREN SEMICOLON
    """


def p_prototype_expr(p):
    """
    PrototypeExpr : PrototypeExpr ProtoType
    | empty
    """


def p_expr(p):
    """
    Expr : LValue EQUAL Expr
    | Constant
    | LValue
    | THIS
    | Call
    | LPAREN Expr RPAREN
    | Expr PLUS Expr
    | Expr MINUS Expr
    | Expr DIVIDE Expr
    | Expr TIMES Expr
    | Expr MODULE Expr
    | MINUS Expr
    | Expr BIGGER_THAN Expr
    | Expr BIGGER_THAN_OR_EQUAL Expr
    | Expr SMALLER_THAN Expr
    | Expr SMALLER_THAN_OR_EQUAL Expr
    | Expr LOGICAL_EQUAL Expr
    | Expr LOGICAL_NON_EQUAL Expr
    | Expr LOGICAL_AND Expr
    | Expr LOGICAL_OR Expr
    | EXCLAMATION Expr
    | READINTEGER LPAREN RPAREN
    | READLINE LPAREN RPAREN
    | NEW T_ID
    | NEWARRAY LPAREN Expr COMMA Type RPAREN
    | ITOD LPAREN Expr RPAREN
    | DTOI LPAREN Expr RPAREN
    | ITOB LPAREN Expr RPAREN
    | BTOI LPAREN Expr RPAREN
    """


def p_expr_expr(p):
    '''
    ExprExpr : ExprExpr COMMA Expr
    | Expr
    '''


def p_l_value(p):
    '''
    LValue : T_ID
    | Expr POINT T_ID
    | Expr LBRACKET Expr RBRACKET
    '''


def p_call(p):
    '''
    Call : T_ID LPAREN Actuals RPAREN
    | Expr POINT T_ID LPAREN Actuals RPAREN
    '''


def p_constant(p):
    '''
     Constant : T_INTLITERAL Constant
     | T_DOUBLELITERAL Constant
     | T_BOOLEANLITERAL Constant
     | T_STRINGLITERAL Constant
     | NULL
    '''


parser = yacc.yacc()

# def make_parser(input_program):
#     logging.basicConfig(
#         level=logging.CRITICAL,
#     )
#     log = logging.getLogger()
#     result = parser.parse(input_program, lexer=lex.lex(module=lexer), debug=log)
#     if parser.errorok:
#         # print("Parsing succeeded")
#         return True
#     else:
#         # print("Parsing failed")
#         return False
