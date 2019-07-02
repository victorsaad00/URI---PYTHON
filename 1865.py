test_cases = int(input())
i = int(0)

while i < test_cases:
    hero = input().split()
    name, force = hero

    if name == 'Thor': print('Y')
    else: print('N')

    i += 1

    