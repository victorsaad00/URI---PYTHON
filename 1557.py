while True:
    matriz = []
    value = 1
    aux = 0
    qtd = int(input())
    if qtd == 0: break
    elif qtd == 1: print(qtd)
    else:
        for i in range(qtd):
            line = []
            for l in range(qtd):
                line.append(value)
                value = value * 2
            matriz.append(line)
            value = matriz[aux][1]
            aux += 1
        length = len(str(matriz[i][l]))
        for line in matriz:
            for element in range(qtd):
                if element < qtd - 1: print('{:{}}'.format(line[element], length), end=' ')
                else: print('{:{}}'.format(line[element], length))
        print()
