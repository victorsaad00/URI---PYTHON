def mdc(num_a, num_b): return num_a if not num_b else mdc(num_b, num_a % num_b)

number = int(input())

for x in range(number):
    numbers = input().split()
    num_a, num_b = int(numbers[0]), int(numbers[1])
    print(mdc(num_a, num_b))