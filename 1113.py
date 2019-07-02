while True:
    n, m = input().split()
    n = int(n)
    m = int(m)

    if n > m:
        print('Decrescente')
    elif n < m:
        print('Crescente')
    elif n == m:
        break