from compiler.lexer import lexer
from compiler.preprocessor import run_preprocess
from compiler.yacc import make_parser


def run_parser(input_file_address):
    with open(input_file_address) as input_file:
        data = input_file.read()
    return make_parser(data)


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

    result = run_parser(input_file_address)
    return result
