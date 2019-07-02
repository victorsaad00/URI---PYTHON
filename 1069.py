test_case = int(input())

for i in range(test_case):
    text = input()
    total = int(0)
    lower = int(0)
    for j in range(len(text)):
        if text[j] == "<": lower +=1
        if text[j] == '>' and lower > 0:
            total += 1
            lower -= 1
    print(total)