nc = int(input())
cont = 0
while cont < nc:
    var = input().split(" ")
    l = [var[0],var[1]]
    l.sort()
    x = int(l[0])
    y = int(l[1])
    cont += 1
    if x % 2 == 0:#se o numero menor for par
        si = 0
        for i in range(x+1,y):#gerar do b+1 ate a
            if i % 2 != 0:#se for impar adiciona no si
                si += i
    else:#se o numero menor for impar
        si = 0
        for i in range(x+2,y):#gerar do b+2 ate a
            if i % 2 != 0:#se for impar adiciona no si
                si += i
    print(si)