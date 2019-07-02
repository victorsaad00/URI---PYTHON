test_cases = int(input())

while test_cases:

    test_cases -= 1
    addrs, keys = [int(x) for x in input().split()]
    hash = {str(x) : [] for x in range(addrs)}
    entry = [int(x) for x in input().split()]


    for i in entry:
        resto = i % addrs
        hash[str(resto)].append(int(i))

    for i in hash:
        print('{} -> '.format(i), end = '')
        for j in hash[i]:
            print('{} -> '.format(j), end = '')
        print('\\')

    print()