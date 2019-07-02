while True:
    ducks = int(input())
    if ducks == int(-1):
        break
    elif ducks == 0:
        print('{}'.format(ducks))
    else:
        ducks-=1
        print('{}'.format(ducks))