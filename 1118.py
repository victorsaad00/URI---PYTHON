_inv_count = int(0)
result = int(0)
count = int(0)
x = int(0)
while x == 0:
    nota = float(input())

    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        result += nota
        count+=1
        if count == 2:
            print('media = {:0.2f}'.format(float(result/2)))
            y = int(0)
            while y == 0:
                inp = int(input('novo calculo (1-sim 2-nao)\n'))
                if inp == 1:
                    y=1
                elif inp == 2:
                    x+=1
                    y+=1
                else:
                    y=0
            count = 0
            result = 0


