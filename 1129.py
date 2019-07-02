while True:
    n = int(input())
    if n == 0: break
    count = int(0)
    while count < n:
        a, b, c, d, e = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        if a >= 0 and a <= 127 and b > 127 and c>127 and d >127 and e > 127:
            print('A')
        elif b >= 0 and b <= 127 and a > 127 and c>127 and d >127 and e > 127:
            print('B')
        elif c >= 0 and c <= 127 and b > 127 and a>127 and d >127 and e > 127:
            print('C')
        elif d >= 0 and d <= 127 and b > 127 and c>127 and a >127 and e > 127:
            print('D')
        elif e >= 0 and e <= 127 and b > 127 and c>127 and d >127 and a > 127:
            print('E')
        else:
            print('*')
        '''
        0 -> black
        255 -> white
        127 <= -> black
        127 > -> white
        '''
        count += 1