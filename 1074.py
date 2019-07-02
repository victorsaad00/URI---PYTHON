max_value = int(input())

i = int(0)
list = [0]*max_value

while i < max_value:
    number = int(input())
    list[i] = number
    i+=1

for i in range(0,len(list)):
    if list[i] < 0:
        if list[i]%2 == 1:
            print('ODD NEGATIVE')
        else:
            print('EVEN NEGATIVE')
    elif list[i] == 0:
        print('NULL')
    else:
        if list[i]%2 == 1:
            print('ODD POSITIVE')
        else:
            print('EVEN POSITIVE')

