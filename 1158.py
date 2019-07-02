test_case = int(input())
count = int(0)
while count < test_case:
    x, y = input().split()
    x = int(x)
    y = int(y)

    i = int(0)
    sum = int(0)
    while i < y:
        if x % 2 != 0:
            sum += x
            i += 1
        x += 1
    print(sum)
    count += 1
