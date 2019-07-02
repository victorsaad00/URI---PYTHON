f = []
even = []
odd = []
numbers = int(input())

while numbers > 0:
    i = int(input())
    if (i % 2 == 0): even.append(i)
    else: odd.append(i)
    numbers -= 1

even.sort()
odd.sort(reverse=True)
for i in even: f.append(i)
for i in odd: f.append(i)

for i in f: print(i)