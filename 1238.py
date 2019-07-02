test_cases = int(input())
i = int(0)

while i < test_cases:
    text = input().split(" ")
    t1,t2 = text
    t_new = ''
    i += 1
    if len(t1) <= len(t2):
        for j in range(len(t1)):
            t_new += t1[j]
            t_new += t2[j]
        t_new += t2[len(t1):]
    else:
        for j in range(len(t2)):
            t_new += t1[j]
            t_new += t2[j]
        t_new += t1[len(t2):]
    print(t_new)
