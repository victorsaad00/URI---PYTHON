_input = int(input())
count = int(0)
is_perfect = int(1)
sum = int(0)
while count < _input:
    number = int(input())
    while is_perfect < number:
        if number % is_perfect == 0:
            sum += is_perfect
            is_perfect += 1
        else: is_perfect += 1
    if sum == number: print('{} eh perfeito'.format(number))
    else : print('{} nao eh perfeito'.format(number))
    is_perfect = 1
    sum = 0
    count += 1