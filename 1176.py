list = [0, 1]
count = 1
while count <= 60:
    list.append(list[-1] + list[-2])
    count += 1
ran = int(input())
for i in range(ran):
    n = int(input())
    print("Fib({:d}) = {:d}".format(n, list[n]))