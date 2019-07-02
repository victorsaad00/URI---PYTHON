S = float(1)
i = int(3)
j = int(2)

while i <= 39:
    S += (i/j)
    i += 2
    j *= 2

print('{:0.2f}'.format(S))