x = int(input())
count = 0

if x <= 10000:
  while count < x:
    w, z = map(int, input().split())
    if w > 0 and z > 0:
      sum = w + z
      print(sum)
    count+=1