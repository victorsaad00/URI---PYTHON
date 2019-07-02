def factorial(number):
    if number == 0: return 1
    elif number == 1: return 1
    else : return number*factorial(number - 1)

def simple_factorial(number):
    if number >= 1: return number*simple_factorial(number-1)
    else: return 1

fatorial = int(input())
print(factorial(fatorial))
print(simple_factorial(fatorial))