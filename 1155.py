num = int(1)
S = float(0)
while num < 100:
    S += 1/num
    num += 1


print('{:0.2f}'.format(S+0.01))