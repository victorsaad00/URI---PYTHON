number = int(input())
'''
def devide(number,i):
    if i <= 100:
        if i%number==2:
            print(i)
            return devide(number, i+1)
        else:
            return devide(number,i+1)


devide(number,1)
'''

for i in range(1,10000):
    if i%number==2:
        print(i)
