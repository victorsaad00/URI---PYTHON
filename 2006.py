tea = int(input())
ans = input()
ans = ans.split(' ')
contestant = int(0)

for i in range(len(ans)):
    if int(ans[i]) == tea: contestant += 1

print(contestant)