test_case = int(input())

for i in range(test_case):
    string = input().upper()
    count = 0
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    for letter in letters:
        if letter in string:
            count += 1

    if count == 26: print('frase completa')
    elif count >= 13: print('frase quase completa')
    else: print('frase mal elaborada')


