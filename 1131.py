inter, gremio = input().split()
inter = int(inter)
gremio = int(gremio)

inter_wins = int(0)
gremio_wins = int(0)
grenials = int(1)
empate = int(0)

if inter > gremio:  # inter_wins
    inter_wins += 1
elif inter < gremio:
    gremio_wins += 1
elif inter == gremio:
    empate += 1

while True:
    print('Novo grenal (1-sim 2-nao)')
    answer = int(input())
    if answer == 1:
        grenials+=1
        inter, gremio = input().split()
        inter = int(inter)
        gremio = int(gremio)
        if inter > gremio:  # inter_wins
            inter_wins += 1
        elif inter < gremio:
            gremio_wins += 1
        elif inter == gremio:
            empate += 1
    else:
        print('{} grenais'.format(grenials))
        print('Inter:{}\nGremio:{}\nEmpates:{}'.format(inter_wins,gremio_wins,empate))
        if inter_wins > gremio_wins:
            print('Inter venceu mais')
        elif inter_wins < gremio_wins:
            print('Gremio venceu mais')
        else:
            print('Não houve vencedor')
        break
