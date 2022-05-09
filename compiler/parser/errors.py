def p_error(p):
    if p is None:
        print("unexpected end of file")
    else:
        print("unexpected token : " + str(p))
