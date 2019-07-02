s = int(0)
biggest = ''
while True:
    list = input().split()
    sizes = []
    if list == ['0']: break

    for i in list:
        sizes.append(str(len(i)))
        if len(i) >= s:
            s = len(i)
            biggest = i
    word_len = '-'.join(sizes)
    print(word_len)

print('')
print('The biggest word: {}'.format(biggest))