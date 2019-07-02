a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

caso_a = float(b) - float(c)
caso_b = float(a) - float(c)
caso_c = float(a) - float(b)

if caso_a < 0 :
    caso_a = (-1)*float(caso_a)
if caso_b < 0:
    caso_b = (-1)*float(caso_b)
if caso_c < 0:
    caso_c = (-1) * float(caso_c)

if a > caso_a and a < (b + c):
    perimetro = a+b+c
    print('Perimetro = {:0.1f}'.format(float(perimetro)))
elif b > caso_b and b < (a+c):
    perimetro = a+b+c
    print('Perimetro = {:0.1f}'.format(float(perimetro)))
elif c > caso_c and c < (a+b):
    perimetro = a+b+c
    print('Perimetro = {:0.1f}'.format(float(perimetro)))
else:
    area = ((a+b)*c)/2
    print('Area = {:0.1f}'.format(float(area)))


