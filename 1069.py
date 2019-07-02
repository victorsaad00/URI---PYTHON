while True:
    try:
        expression = input()
        balance = int(0)
        for i in range(len(expression)):
            if expression[i] == '(': balance += 1
            elif expression[i] == ')': balance -= 1
            if balance < 0: break
        if balance != 0: print('incorrect')
        else: print('correct')

    except EOFError: break