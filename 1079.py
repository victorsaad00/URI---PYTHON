qtd = int(input())
avarage = float(0)
avarage_list = [0]*qtd
for i in range(0,qtd):
    number = input().split()
    avarage = (float(number[0])*2 + float(number[1])*3 + float(number[2])*5)/10
    avarage_list[i] = float(avarage)
for i in range(0,len(avarage_list)):
    print('{:0.1f}'.format(avarage_list[i]))
