'''
def fibonacci(number):
    if number == 1 or number == 0: return 1
    else: return fibonacci(number - 1) + fibonacci(number - 2)
    
i = int(0)
while i < fib - 1:
    if i == 0:
        print('0',end=" ")
    print('{}'.format(fibonacci(i)),end=" ")
    i+=1
'''

fib = int(input())
t1 = int(0)
t2 = int(1)
print('{} {}'.format(t1,t2),end=" ")

count = int(3)
while count <= fib:
    t3 = t1 + t2
    print('{}'.format(t3), end=" ")
    t1 = t2
    t2 = t3
    count+=1

