_min = int(10)
list = []*10

def find_max(_list):
    _max = _list[0]
    for i in range(0,len(_list)):
        if _max <= _list[i]:
            _max = list[i]
    return _max

def _position(list,max):
    for i in range(0,len(list)):
        if max == list[i]:
            return i+1


while _min > 0:
    number = int(input())
    list.append(number)
    _min -= 1

maximum = find_max(list)
print('{}\n{}'.format(int(maximum),int(_position(list,maximum))))

