while True:
    number = int(input())
    if number == 0: break

    list = input().split()

    for i in range(number):
        list[i] = int(list[i])

    list_r = sorted(list, key=int)

    for killer, i in enumerate(list):
        if i < list_r[number - 2]:
            print(killer + 1)
            break