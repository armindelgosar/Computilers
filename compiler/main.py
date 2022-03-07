from compiler.preprocessor import run_preprocess
from compiler.lexer import lexer
from dotenv import load_dotenv


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

        if(token.lineno == skipLineNo):
            continue

        if(token.type == "DEFINE"):
            skipLineNo = token.lineno
            continue

        if(token.type.startswith("T_")):
            result += token.type + " " + str(token.value) + "\n"
            print(token.type + " " + str(token.value))
        else:
            result += str(token.value) + "\n"
            print(str(token.value))

    return result

if __name__ == '__main__':
    load_dotenv('../.env')
    run(input_file_address=env['SCANNER_INPUT_FILE_ADDRESS'])
