test_cases = int(input())
while test_cases:
    test_cases -= 1
    gifts, max_weight = [int(i) for i in input().split()]
    gift_weight = [int(i) for i in input().split()]
    travels = 1
    i = 1
    weight = gift_weight[0]
    while i < gifts:
        if weight + gift_weight[i] > max_weight:
            travels += 1
            weight = gift_weight[i]
        else:
            weight += gift_weight[i]

        i += 1

    print(travels)