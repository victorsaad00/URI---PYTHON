while True:
    number = input()

    if number == '-1': break

    if number.isdigit():

        number = hex(int(number))
        number = number[:2] + number[2:].upper()

    else: number = int(number, 16)

    print(number)