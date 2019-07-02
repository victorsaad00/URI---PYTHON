a = int(input())

b = int(input())
c = int(input())

d = int(input())
e = int(input())

list = [a,b,c,d,e]


even = int(0)
odds = int(0)
neg = int(0)
pos = int(0)
zero = int(0)
for i in range(0,len((list))):
    if list[i] < 0:
        neg += 1
    elif list[i] == 0:
        zero+=1
    else:
        pos += 1
for j in range(len(list)):
    if list[j]%2 != 0:
        odds+=1
    else:
        even+=1


print('{} valor(es) par(es)'.format(even))
print('{} valor(es) impar(es)'.format(odds))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
