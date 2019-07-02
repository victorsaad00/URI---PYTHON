number = 0
positive_count = 0
avarage = float(0)
addition = float(0)
for i in range(1,7):
    number = float(input())
    if number > 0:
        addition+=number
        positive_count+=1

avarage = addition / positive_count
print('{} valores positivos'.format(int(positive_count)))
print('{:0.1f}'.format(float(avarage)))

