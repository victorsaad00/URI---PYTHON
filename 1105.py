while True:
    b, n = input().split()
    b = int(b) # number of banks
    n = int(n) # number of debentures
    if b == 0 or n == 0: break

    test = int(0)
    reserves = []*b
    d = int(0)
    c = int(0)
    v = int(0)
    for i in range(0,b):
        d,c,v = input().split()
        d = int(d)
        c = int(c)
        v = int(v)

        reserves[d] -= v
        reserves[c] += v

    print(reserves)