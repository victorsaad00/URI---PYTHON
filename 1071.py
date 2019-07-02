x = int(input())
y = int(input())

def function(x,y):
    if y < x:
        i=int(0)
        while (y + 1) < x:
            y+=1
            if y % 2 != 0:
                i += y
        return i
    else: # x < y
        i = int(0)
        while x + 1 < y:
            x += 1
            if x % 2 != 0:
                i += x
        return i


print(function(x,y))
