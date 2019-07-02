array = [float]*100
i = int(0)

while i < 100:
    number = float(input())
    array[i] = number
    i += 1

for i in range(0, len(array)):
    if array[i] <= 10: print('A[{}] = {:0.1f}'.format(i, array[i]))