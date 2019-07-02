a,b,c = input().split()

if (int(a) > int(b)) and (int(a) > int(c)) :
    maior = int(a)
elif (int(b) > int(c)) and (int(b) > int(c) ):
    maior = int(b)
else :
    maior = int(c)

print("%d eh o maior"%maior)
