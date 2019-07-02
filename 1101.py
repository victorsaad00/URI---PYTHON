def my_print(n,m):
    if n < m: # 3 6
        list = [0]*(m - n + 1)
        i = int(0)
        while i < len(list):
            list[i] = n
            n += 1
            i += 1
        return list
    else :
        list = [0]*(n - m + 1)
        i = int(0)
        while i < len(list):
            list[i] = m
            m += 1
            i += 1
        return list

def _sum(n,m):
    temp = int(0)
    count = int(0)
    if n < m:
        count = n
        temp = int(n)
        while n < m:
            n += 1
            temp += n
    elif m < n:
        count = m
        temp = int(m)
        while m < n:
            m += 1
            temp += m
    return temp

while True:
    list = input().split()
    n, m = [int(i) for i in list]
    if n == 0 and m != 0 or m == 0 and n!=0:
        break
    else:
        lista = my_print(n,m)
        lista.append("Sum="+str(_sum(n,m)))
        for i in lista:
            print(i, end=" ")
