import logging

from compiler.preprocessor import run_preprocess
from compiler.yacc import parser


def run(input_file_address: str) -> bool:
    result = ''
    with open(input_file_address) as input_file:
        data = input_file.read()
    data = run_preprocess(input_data=data)
    logging.basicConfig(
        level=logging.CRITICAL,
    )
    log = logging.getLogger()
    try:
        res = parser.parse(input=data, debug=True)
        # return True
        return "OK"
    except SyntaxError as e:
        return "Syntax Error"
        #return False
