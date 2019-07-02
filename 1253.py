test_cases = int(input())

for i in range(test_cases):
    string = input()
    test_cases = int(input())
    crypto = ''
    for j in string:
        pos = ord(j) - test_cases

        if pos < 65: crypto += chr(91 - (65 - pos))
        else: crypto += chr(ord(j) - test_cases)

    print(crypto)