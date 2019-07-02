while True:
    try:
        _lines = ""
        lines = input()
        uppercase = True

        for l in lines:
            if l == ' ':
                _lines += ' '
                continue
            if uppercase:
                _lines += l.upper()
                uppercase = False
            else:
                _lines += l.lower()
                uppercase = True
        print(_lines)
    except EOFError: break