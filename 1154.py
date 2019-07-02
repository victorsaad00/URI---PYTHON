i = int(0)
avg = float(0)
while True:
    number = float(input())
    if number >= 0:
        avg += number
        i += 1
    else:
        print('{:0.2f}'.format(avg / i))
        break





