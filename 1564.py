x = 0
test = []
while True:
    try:
        x = int(input())
        test.append(x)
    except EOFError: break
for i in test[0:len(test)]:
    if i == 0: print("vai ter copa!")
    else: print("vai ter duas!")