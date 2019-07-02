n = int(input())
m = int(input())
result = int(0)

if n < m:
    while n <= m:
        if n%13 != 0: # nao e multiplo
            result+=n
        n+=1
else:
    while m <= n:
        if m%13 != 0: # nao e multiplo
            result+=m
        m+=1

print(result)