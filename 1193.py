test_cases = int(input())
count = int(0)

while count < test_cases:

    number, num_typ = input().split()
    dec = 'dec'
    hexi = 'hex'
    binary = 'bin'

    if num_typ == 'bin':

        a = int(number, 2)
        b = hex(int(number, 2))
        b = b[2::]


    elif num_typ == 'dec':

        a = hex(int(number))
        a = a[2::]
        b = bin(int(number))
        b = b[2::]
        dec = hexi
        hexi = binary

    elif num_typ == 'hex':

        a = int(number, 16)
        b = bin(int(number, 16))
        b = b[2::]
        hexi = binary

    print('Case {}:'.format(count+1))
    print('{} {}'.format(a, dec))
    print('{} {}'.format(b, hexi))
    print()
    count +=1