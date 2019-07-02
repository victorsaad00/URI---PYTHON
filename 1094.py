n = int(input())
count = int(0)
i = int(0)

coelho = int(0)
rato = int(0)
sapo = int(0)

while count < n:
    animal = input().split()
    if animal[1] == 'C':
        coelho += int(animal[0])
    elif animal[1] == 'R':
        rato += int(animal[0])
    else:
        sapo += int(animal[0])
    count+=1

total_cobaias = coelho + rato + sapo
_per_r = (rato / int(total_cobaias))*100
_per_c = (coelho / int(total_cobaias))*100
_per_s = (sapo / int(total_cobaias))*100

print('Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\nPercentual de coelhos: {:0.2f} %\nPercentual de ratos: {:0.2f} %\nPercentual de sapos: {:0.2f} %'.format(int(total_cobaias),coelho,rato,sapo,float(_per_c),float(_per_r),float(_per_s)))