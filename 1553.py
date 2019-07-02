while True:
    questions, times = input().split()
    if questions == '0' and times == '0': break

    q_asked = [int(i) for i in input().split()]
    total = 0

    for i in set(q_asked):
        if q_asked.count(i) >= int(times):
            total += 1
    print(total)