lista = list(map(int, input().split()))
num_1 = 'not zero or negative'
num_2 = int(0)
result = int(0)

for i in lista:
    if num_1 == 'not zero or negative':
        num_1 = i
    else:
        if i > 0:
            num_2 = i
            break

for i in range(num_2):
    result += num_1
    num_1 += 1

print("{}".format(result))