keyboard = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
while True:
    try:
        _input = input()
        _key_gem = ''
        for i in _input:
            if i == ' ': _key_gem += i
            else: _key_gem += keyboard[keyboard.index(i)-1]
        print(_key_gem)
    except EOFError: break