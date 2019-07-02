while True:
    try:
        sequence = input()
        cpf = ''
        b1 = 0
        b2 = 0
        for i in range(0,len(sequence)):
            if i % 3 == 0 and i > 0: cpf += '.'
            cpf += sequence[i]
            b1 += int(sequence[i]) * (i + 1)
            b2 += int(sequence[i]) * (9 - i)
        cpf += '-'
        b1 = b1 % 11
        b2 = b2 % 11
        if b1 == 10: b1 = 0
        if b2 == 10: b2 = 0

        cpf += str(b1) + str(b2)

        print(cpf)

    except EOFError: break



