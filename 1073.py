number = int(input())

for i in range (1,number+1):
    if i%2 == 0:
        result = i
        i*=i
        print('{}^2 = {}'.format(int(result),int(i)))