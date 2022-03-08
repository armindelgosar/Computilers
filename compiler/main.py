from compiler.lexer import lexer
from compiler.preprocessor import run_preprocess


def run(input_file_address: str) -> str:
    result = ''

    with open(input_file_address) as input_file:
        data = input_file.read()
    data = run_preprocess(input_data=data)
    lexer.input(data)
    skipLineNo = -1
    while True:
        token = lexer.token()
        if not token:
            break

        if (token.lineno == skipLineNo):
            continue

        if (token.type == "DEFINE"):
            skipLineNo = token.lineno
            continue

        if (token.type.startswith("T_")):
            result += token.type + " " + str(token.value) + "\n"
            print(token.type + " " + str(token.value))
        else:
            result += str(token.value) + "\n"
            print(str(token.value))

    return result


