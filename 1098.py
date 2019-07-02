i = float(0)
j = float(1.0)

a = float(0)
b = float(0)

while i < 2.1:
    while j <= 3.0:
        if (0 < i < 1) or (1 < i < 1.8):
            print('I={:0.1f} J={:0.1f}'.format(i,i+j))
        else:
            a = i
            b = i + j
            print('I={:.0f} J={:.0f}'.format(a,b))
        j+=1
    j = 1
    i += 0.2
