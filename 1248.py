test_case = int(input())
i = int(0)

while i < test_case:
    i += 1
    diet = input()
    coffee = input()
    lunch = input()
    lunch += coffee
    for letra in range(len(lunch)):
        if lunch[letra] not in diet:
            diet = 'CHEATER'
            break
        else: diet = diet.replace(lunch[letra], '')

    if diet != 'CHEATER': diet = ''.join(sorted(diet))
    print(diet)