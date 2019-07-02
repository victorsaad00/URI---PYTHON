def digit(op):
    if not op.isdigit(): return True
    else: return False

while True:
    try:
        operation = input()
        operation = operation.replace('=', '+')
        operation = operation.split('+')
        result = int(0)

        if digit(operation[0]):
            result = int(operation[2]) - int(operation[1])
        elif digit(operation[1]):
            result = int(operation[2]) - int(operation[0])
        elif digit(operation[2]):
            result = int(operation[0]) + int(operation[1])

        print(result)

    except EOFError: break