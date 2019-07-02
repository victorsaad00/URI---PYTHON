import math
a,b,c = input().split()

delta = float(b)*float(b) - float(float(4*float(a)*float(c)))

if delta < 0 or float(a) <= 0:
    print("Impossivel calcular")
else:
    sqrt_delta = math.sqrt(float(delta))
    x1 = (((-1)*float(b)) + float(sqrt_delta))/(2*float(a))
    x2 = (((-1)*float(b)) - float(sqrt_delta))/(2*float(a))
    print("R1 = {:0.5f}\nR2 = {:0.5f}".format(float(x1),float(x2)))