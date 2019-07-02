a,b,c = input().split()
arr = [float(a),float(b),float(c)]

def bubble_sort(arr):
    temp = 0
    for i in range(len(arr)-1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

bubble_sort(arr)

A = float(arr[0])
B = float(arr[1])
C = float(arr[2])

if A >= (B+C) :
    print('NAO FORMA TRIANGULO')
elif (A*A) == (B*B) + (C*C):
    print('TRIANGULO RETANGULO')
elif (A*A) > ((B*B) + (C*C)):
    print('TRIANGULO OBTUSANGULO')
elif (A*A) < (B*B) + (C*C):
    print('TRIANGULO ACUTANGULO')
if A == B == C:
    print('TRIANGULO EQUILATERO')
if A == B and C != A and C != B:
    print('TRIANGULO ISOSCELES')
if A == C and B != A and B != C:
    print('TRIANGULO ISOSCELES')
if C == B and A != B and A != C:
    print('TRIANGULO ISOSCELES')

