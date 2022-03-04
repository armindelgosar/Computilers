from compiler.lexer import lexer
from os import environ as env
from dotenv import load_dotenv


def run(input_file_address: str) -> None:
    with open(input_file_address) as input_file:
        data = input_file.read()

    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break  # No more input
        print(token)


if __name__ == '__main__':
    load_dotenv('../.env')
    run(input_file_address=env['SCANNER_INPUT_FILE_ADDRESS'])
