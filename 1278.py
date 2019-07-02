check = 0
while True:
    lines = int(input())
    if lines == 0: break
    if check == 1: print()

    test = []
    for i in range(lines):
        test.append(' '.join(input().split()))
    m = max(len(i) for i in test)

    for i in range(len(test)):
        for j in range(m-len(test[i])):
            print('', end=' ')

        print(test[i])

    check = 1