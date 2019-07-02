import math
number_one, number_two = input().split()
number_one = int(number_two) - int(number_one)
number_one = math.ceil(int(number_two) / number_one)
print(number_one)