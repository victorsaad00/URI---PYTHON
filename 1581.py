test_case = int(input())
count = int(0)

while count < test_case:
    count += 1
    list = []
    ppl_group = int(input())
    i = int(0)
    while i < ppl_group:
        i += 1
        list.append(input())

    main = list[0]
    for ppl_group in list:
        if ppl_group != main:
            main = 'ingles'
            break

    print(main)