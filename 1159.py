while True:
    x= int(input())
    if x == 0 : break
    i = int(0)
    sum = int(0)
    while i < 5:
        if x % 2 == 0:
            sum += x
            i += 1
        x += 1
    print(sum)

