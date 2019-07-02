'''import re

test_cases = int(input())

for i in range(test_cases):
    text = input()
    new_text = ''

    for l in text:
        if re.match("[a-zA-Z]", l): new_text += chr(ord(l) + 3)
        else: new_text += l

    new_text = new_text[::-1]
    half = int((len(new_text) / 2))
    first = new_text[0:half]
    sec = new_text[half:]
    new_half = ''

    for l in sec: new_half += chr(ord(l) - 1)

    crypto = first + new_half
    print(crypto)'''
import math

test_cases = int(input())
for i in range(test_cases):
    text = str(input())

    text2 = ''
    for x in text:
        if x.isalpha(): text2 += chr(ord(x) + 3)
        else: text2 += x

    text3 = text2[::-1]
    s = math.ceil(len(text3) / 2)
    text4 = text3[-s:]
    text5 = ''
    for y in text4: text5 += chr(ord(y) - 1)
    crypto = text3.replace(text4, text5)
    print(crypto)


