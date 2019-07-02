
ppl_torture = int(input())
x = input().split()

for i in range(ppl_torture):
    x[i] = int(x[i])

menor = min(x)
persons = x.index(menor) + 1




print(persons)