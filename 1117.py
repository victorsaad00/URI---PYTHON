_inv_count = int(0)
result = int(0)
count = int(0)
while True:
    nota = float(input())

    if nota < 0 or nota > 10:
        print('nota invalida')
        _inv_count+=1
    else:
        result += float(nota)
        count+=1
        if count == 2:
            print('media = {}'.format(float(result/2)))
            count = 0
            result = 0
        if _inv_count >= 2:
            break






