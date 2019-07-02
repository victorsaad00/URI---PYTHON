test_case = int(input())
let = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 's', 'S']


while test_case > 0:
    test_case -= 1
    characters = input()
    var = 1

    for i in range(len(characters)):
        if characters[i] in let: var *= 3
        else: var *= 2

    print(var)