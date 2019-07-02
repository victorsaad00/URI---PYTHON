var = input()
animal = str(input())
alimentacao = str(input())

if var == 'vertebrado':
    if animal == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if alimentacao == 'onivoro':
            print('homem')
        else:
            print('vaca')
elif var == 'invertebrado':
    if animal == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        else :
            print('lagarta')
    else:
        if alimentacao == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')


