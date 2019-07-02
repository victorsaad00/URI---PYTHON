def possible(a, b, c):
    if abs(b - c) < a < (b + c):
        if abs(a - c) < b < (a + c):
            if abs(a - b) < c < (a + b): return True
    else: return False

def triangle(a, b, c, d):
    if possible(a, b, c) or possible(a, b, d) \
    or possible(a, c, d) or possible(b, c, d): print('S')
    else: print('N')

a, b, c, d = map(int, input().split())
triangle(a, b, c, d)

