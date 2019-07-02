A,B,C = input().split()
pi = 3.14159

area_triangulo = (float(A)*float(C))/2
area_circulo = pi * (float(C)*float(C))
area_trapezio = (((float(A)+float(B))* float(C)) /2)
area_quadrado = float (B) * float(B)
area_retangulo = float (A) * float(B)

print("TRIANGULO: %0.3f" %(area_triangulo))
print("CIRCULO: %0.3f" %(area_circulo))
print("TRAPEZIO: %0.3f" %(area_trapezio))
print("QUADRADO: %0.3f" %(area_quadrado ))
print("RETANGULO: %0.3f" %(area_retangulo))
