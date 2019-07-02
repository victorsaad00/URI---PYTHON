while True:
    try:
        divers, diver_r = input().split()
        divers = int(divers)
        diver_r = int(diver_r)
        returned = [int(i) for i in input().split()]
        if divers - diver_r == 0:
            print("*")
        else:
            no_returned = []

            for i in range(1, divers + 1):
                if i not in returned:
                    no_returned.append(i)

            for i in no_returned: print(i, end=' ')

            print()
    except Exception:
        break