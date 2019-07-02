test_cases = int(input())
count = int(0)

while count < test_cases :

    message = input()
    m = int(len(message) / 2) - 1
    out = message[m::-1] + message[len(message) - 1:m:-1]
    print(out)
    count += 1