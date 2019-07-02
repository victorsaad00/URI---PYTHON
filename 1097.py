i = int(1)
j = int(7)
t = int(0)
while i <= 9:
    while t < 3:
        print('I={} J={}'.format(i, j))
        j -= 1
        t += 1
    i += 2
    j += 5
    t = 0
