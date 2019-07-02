while True:
    entry = int(input())
    i = int(1)
    if entry == 0:
        break
    else:
        while i <= entry:
            if i == entry:
                print(i)
                break
            else:
                print('{}'.format(i),end=" ")
                i += 1