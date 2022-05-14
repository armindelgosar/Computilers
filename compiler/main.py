from compiler import lexer as yacc_lexer
from compiler.lexer import lexer
from compiler.preprocessor import run_preprocess
# from compiler.parser.yacc import make_parser
from compiler.parser.yacc import parser
import ply.lex as lex



def run_parser(input_file_address):
    with open(input_file_address) as input_file:
        data = input_file.read()
        result = parser.parse(data, lexer=lex.lex(module=yacc_lexer))
        if parser.errorok:
            # print("Parsing succeeded")
            return True
        else:
            # print("Parsing failed")
            return False


# return make_parser(data)



def run(input_file_address: str) -> bool:
    result = ''
    with open(input_file_address) as input_file:
        data = input_file.read()
    data = run_preprocess(input_data=data)
    lexer.input(data)
    skip_line_no = -1
    while True:
        token = lexer.token()
        if not token:
            break

        if token.lineno == skip_line_no:
            continue

        if token.type == "DEFINE":
            skip_line_no = token.lineno
            continue

        if token.type.startswith("T_"):
            result += token.type + " " + str(token.value) + "\n"
            # print(token.type + " " + str(token.value))
        else:
            result += str(token.value) + "\n"
            # print(str(token.value))

    return run_parser(input_file_address)
