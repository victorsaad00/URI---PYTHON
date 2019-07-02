while True:
    try:
        entry = input()
        i = 0
        b = 0
        result = ''
        for j in range(len(entry)):

            if entry[j] == '_':
                if i == 0:
                    result += '<i>'
                    i = 1
                else:
                    result += '</i>'
                    i = 0
            elif entry[j] == '*':
                if b == 0:
                    result += '<b>'
                    b = 1
                else:
                    result += '</b>'
                    b = 0
            else: result += entry[j]
        print(result)

    except EOFError: break