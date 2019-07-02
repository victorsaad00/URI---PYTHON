while True:
    limit = int(input())
    if limit == 0: break
    results =  []

    for i in range(1, (limit + 1)):
        tmp = []
        count = i
        for j in range(limit):
            tmp.append(abs(count))
            if(count == 1):
                count -= 3
            else:
                count -= 1
        results.append(tmp)

    for i in range(limit):
        tx = ''
        for j in range(limit):
            tx += " %3d" % results[i][j]
        print(tx[1:])
    print("")