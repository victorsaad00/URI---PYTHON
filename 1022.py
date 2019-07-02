def common_div(n, m):
    if m == 0:
        return n
    else:
        return common_div(m, n % m)

test_cases = int(input())
count = int(0)
while count < test_cases:
    exp = input().split()
    print(exp)
    num_1 = int(exp[0])
    num_2 = int(exp[4])
    operation = str(exp[3])
    denomi_1 = int(exp[2])
    denomi_2 = int(exp[6])
    num = int(0)
    den = int(1)

    if operation == '+':
        num = (num_1 * denomi_2 + num_2 * denomi_1)
        den = (denomi_1 * denomi_2)
    elif operation == '-':
        num = (num_1 * denomi_2 - num_2 * denomi_1)
        den = (denomi_1 * denomi_2)
    elif operation == '*':
        num = (num_1 * num_2)
        den = (denomi_1 * denomi_2)
    elif operation == '/':
        num = (num_1 * denomi_2)
        den = (num_2 * denomi_1)

    print('{:0.0f}/{:0.0f} = {:0.0f}/{:0.0f}'.format(num, den, num / common_div(num, den), den / common_div(num, den)))
    count += 1
