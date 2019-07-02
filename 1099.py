nc = int(input())
cont = int(0)
si = int(0)

while cont < nc:
    var = input().split()
    var.sort()
    x = int(var[0])
    y = int(var[1])
    if x % 2 == 0:
        for i in range(x+1,y):
            if i % 2 != 0:
                si += i
    else:
        for i in range(x+2,y):
            if i % 2 != 0:
                si += i
    cont += 1
    print(si)
    si = 0
