x, y, z = input().split()
arr = [int(x),int(y),int(z)]
arr2 = [int(x),int(y),int(z)]

def merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_Sort(L)
        merge_Sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def print_list(arr):
    print('{}'.format(arr[0]))
    print('{}'.format(arr[1]))
    print('{}'.format(arr[2]))

merge_Sort(arr)

print_list(arr)
print('')
print_list(arr2)