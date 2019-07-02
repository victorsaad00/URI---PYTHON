test_cases = int(input())

while test_cases > 0:
    test_cases -= 1
    sheeps = int(input())

    c = [int(x) for x in input().split()]

    print(len(set(c)))