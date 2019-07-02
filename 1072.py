n = int(input())

_in = 0
_out = 0

for i in range(n):
    num = int(input())
    if 10 <= num <= 20:
        _in+= 1
    else:
        _out+=1

print('{} in'.format(int(_in)))
print('{} out'.format(int(_out)))
