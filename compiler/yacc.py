import ply.yacc as yacc
import logging
from compiler.lexer import tokens
from compiler.lexer import lexer

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




def p_constants(p):
    '''Constants : T_INTLITERAL
    | T_DOUBLELITERAL
    | T_BOOLEANLITERAL
    | T_STRINGLITERAL
    | NULL
    '''
    # semantic


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

def p_empty(p):
    'empty :'
    pass

# def p_error(p):
#     if p is None:
#         print("unexpected end of file")
#     else:
#         print("unexpected token : " + str(p))


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
    '''Stmt : Expr SEMICOLON
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
    'PrintStmt : Print LPAREN PrintExpr RPAREN SEMICOLON'
    # semantic
