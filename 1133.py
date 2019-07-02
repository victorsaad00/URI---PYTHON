x = int(input())
y = int(input())


if x <= y: # x -> y > y larger than x
    x+=1
    while x <= y:
        if x%5 == 2 or x%5 == 3:
            print('{}'.format(x))
            x+=1
        else:
            x+=1
else:
    y+=1
    while y <= x:
        if y%5 == 2 or y%5 == 3:
            print('{}'.format(y))
            y+=1
        else:
            y+=1