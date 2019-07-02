print(ord('`'))

while True:
    try:
        string = input()
        for letter in string:
            pos = ord(letter)

            if letter >= 'a' and letter <= 'z':
                if pos + 13 > ord('z') : print('{}'.format(chr(pos - 13)), end = '')
                else: print('{}'.format(chr(pos + 13)), end = '')
            elif letter >= 'A' and letter <= 'Z':
                if pos + 13 > ord('Z'): print('{}'.format(chr(pos - 13)), end='')
                else: print('{}'.format(chr(pos + 13)), end='')
            else: print('{}'.format(letter), end='')
        print()
    except EOFError: break

