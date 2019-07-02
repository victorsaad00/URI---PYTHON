x, y, z = input().split()
arr = [int(x),int(y),int(z)]
arr2 = [int(x),int(y),int(z)]

def bubble_sort(arr):
    temp = 0
    for i in range(len(arr)-1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def print_list(arr):
    print('{}'.format(arr[0]))
    print('{}'.format(arr[1]))
    print('{}'.format(arr[2]))

bubble_sort(arr)

print_list(arr)
print('')
print_list(arr2)