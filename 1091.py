while True:
    k = int(input())
    if k <= 0: break
    n,m = input().split()
    n = int(n)
    m = int(m)
    count = int(0)
    while count < k:
        x, y = input().split()
        x = int(x)
        y = int(y)
        if x > n and y > m:
            print('NE')
        elif x > n and y < m:
            print('SE')
        elif x < n and y > m:
            print('NO')
        elif x < n and y < m:
            print('SO')
        elif x == n or y == m:
            print('divisa')
        count += 1
