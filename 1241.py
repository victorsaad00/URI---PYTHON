test_case = int(input())
i = int(0)

while i < test_case:
    i += 1
    a, b = input().split()

    if len(a) < len(b) : print('nao encaixa')
    else:
        if a[len(a)-len(b)::] == b : print('encaixa')
        else: print('nao encaixa')