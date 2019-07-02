test_case = int(input())

while test_case > 0:
    test_case -= 1

    students = int(input())
    grade = input().split()

    for ind, i in enumerate(grade): grade[ind] = int(grade[ind])

    b = sorted(grade)
    b.reverse()
    total = 0

    for ind, i in enumerate(grade):
        if grade[ind] == b[ind]: total +=1

    print(total)