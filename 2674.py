import math

def is_prime(num):
    if num < 0:
        return False
    n = int(math.sqrt(num))
    if num % 2 == 0 and num != 2 or num == 1:
        return False
    else:
        for i in range(3, n + 1, 2):
            if num % i == 0:
                return False
    return True

def is_super(number):
    split_number = [int(i) for i in str(number)]
    count = int(0)
    for i in range(0, len(split_number)):
        if is_prime(split_number[i]):
            count += 1
    if count >= len(split_number):
        return True
    else:
        return False

while True:
    try:
        number = int(input())
        if number == 2 or number == 3 or number == 5 or number == 7:
            print('Super')
        else:
            if is_super(number) and is_prime(number):
                print('Super')
            elif is_prime(number):
                print('Primo')
            else:
                print('Nada')

    except EOFError:
        break