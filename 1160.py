t = int(input())
for i in range(t):
    time = 0
    x = input().split()
    a, b, ga, gb = [float(n) for n in x]
    a = int(a)
    b = int(b)
    if a < b <= 1000000:
        while a <= b:
            a += int((a*(ga/100)))
            b += int((b*(gb/100)))
            time += 1
            if time > 100:
                print("Mais de 1 seculo.")
                break
        if time <= 100:
            print("{:d} anos.".format(time))
