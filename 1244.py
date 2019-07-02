test_case = int(input())
count = int(0)

while count < test_case:
    count += 1
    frase = input().split()
    frase.sort(key=len, reverse=True)

    for i in range(len(frase)):
        print(frase[i], end ='')
        if i != len(frase)-1:
            print(' ', end = '')
    print()