while True:
    try:
        leefs = int(input())
        for i in range(1, leefs + 1, 2):
            print((leefs - i) // 2 * ' ', end='')
            print('*' * i)

        print(leefs // 2 * ' ', end='')
        print('*')
        print(((leefs // 2) - 1) * ' ', end='')
        print('***')
        print()

    except EOFError: break