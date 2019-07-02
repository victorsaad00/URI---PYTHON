ddd = int(input())

ddd_estado = {
    int(61) : 'Brasilia',
    int(71) : 'Salvador',
    int(11) : 'Sao Paulo',
    int(21) : 'Rio de Janeiro',
    int(32) : 'Juiz de Fora',
    int(19) : 'Campinas',
    int(27) : 'Vitoria',
    int(31) : 'Belo Horizonte'
}

if ddd_estado.get(ddd) == None:
    print('DDD nao cadastrado')
else:
    print(ddd_estado.get(ddd))