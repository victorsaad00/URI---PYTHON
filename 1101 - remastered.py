while True:
    n,m = input().split()
    n = int(n)
    m = int(m)
    c = int(0)
    if n <= 0 or m <= 0:
        break
    else:
        d = int(0)
        if n < m:
            c = n
            for i in range(c,m+1):
                print(i, end=' ')
                d += i
            print("Sum={}".format(d))
        else:
            c = m
            for i in range(c,n+1):
                print(i, end=' ')
                d += i
            print("Sum={}".format(d))