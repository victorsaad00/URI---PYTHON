a, b = [int(x) for x in input().split()]

for i in range(abs(b)):
    if (a - i) % b == 0:
        result = int((a - i) / b)
        break

print(result, i)