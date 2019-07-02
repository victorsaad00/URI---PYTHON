_one = int(input())
_two = int(0)

while True:
    _two = int(input())
    if _two > _one : break

sum = _one
i = int(1)
while sum < _two:
    sum += _one + i
    i += 1

print(i)