array = [int]*10
count = int(0)
i = int(0)
while count < 10:
    number = int(input())
    if number <= 0:
        array[i] = 1
        print('X[{}] = {}'.format(i, array[i]))
    else:
        array[i] = number
        print('X[{}] = {}'.format(i, array[i]))
    count += 1
    i += 1
