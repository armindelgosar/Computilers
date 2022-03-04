from ply.yacc import yacc

from compiler.lexer import lexer
from os import environ as env
from dotenv import load_dotenv


# run scanner method
def run(input_file_address: str) -> None:
    with open(input_file_address) as input_file:
        data = input_file.read()
    # data = '3'
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break  # No more input
        print(token)


if __name__ == '__main__':
    # we have a .env file that put our fixed strings on it.
    load_dotenv('../.env')
    # runnable part of project

    # run preprocessor

    # run scanner
    run(input_file_address=env['SCANNER_INPUT_FILE_ADDRESS'])
