def matrix():
    n = int(input())
    m = list()
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append('0')
    return n, m


def diagonal(n, m):
    for i in range(n):  m[i][i] = '2'
    for i in range(n):  m[i][n - 1 - i] = '3'
    return m


def matrix_1(n, m):
    for i in range(n // 3, n - n // 3):
        for j in range(n // 3, n - n // 3):
            m[i][j] = '1'
    return m


def matrix_4(n, m):
    m[n // 2][n // 2] = '4'
    return m


def print_matrix(n, m):
    for i in range(n):
        M = ''.join(m[i])
        print(M)
    print()


def main():
    while True:
        try:
            n, m = matrix()
            m = diagonal(n, m)
            m = matrix_1(n, m)
            m = matrix_4(n, m)
            print_matrix(n, m)
        except EOFError:
            break

main()
