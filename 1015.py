import math

x1,y1 = input().split()
x2,y2 = input().split()

x_minus = float(x2) - float(x1)
x_pot = float(x_minus) * float(x_minus)

y_minus = float(y2) - float(y1)
y_pot = float(y_minus) * float(y_minus)

x_plus_y = float(x_pot) + float(y_pot)

distance = math.sqrt(x_plus_y)
print("%0.4f"%distance)






