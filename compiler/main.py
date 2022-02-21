from .lexer import new_lexer


def run(input_file_address: str) -> str:
    lexer = new_lexer()
    result = ''

    with open(input_file_address) as input_file:
        input_file.read()

    while True:
        token = lexer.token()
        result += token

    return result
