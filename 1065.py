a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list = [a,b,c,d,e]
even = int(0)
for j in range(len(list)):
    if list[j]%2 == 0:
        even+=1

print('{} valores pares'.format(even))


