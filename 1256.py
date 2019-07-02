test_cases = int(input())

for a in range(test_cases):
    hash = []
    addrs, keys = input().split(' ')
    addrs, keys = int(addrs), int(keys)

    for i in range(addrs):
        hash.append([])

    N = input().split(' ')
    I = [int(t) for t in N]

    for t in I:
        p = t % addrs
        hash[p].append(t)

    for p, i in enumerate(hash):
        print('{} -> '.format(p), end='')
        for j in i:
            print('{} -> '.format(j), end='')
        print('\\')
    if a != test_cases - 1:
        print()


