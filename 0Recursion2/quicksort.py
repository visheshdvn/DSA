def partition(array, li, ei):
    pivot = array[li]
    l = li + 1
    h = ei

    while True:
        while l <= h and array[h] >= pivot:
            h = h - 1

        while l <= h and array[l] <= pivot:
            l = l + 1

        if l <= h:
            array[l], array[h] = array[h], array[l]
        else:
            break

    array[li], array[h] = array[h], array[li]

    return h

def quickSort(array, li, ei):
    if li >= ei:
        return
    
    p = partition(array, li, ei)
    quickSort(array, li, p-1)
    quickSort(array, p+1, ei)
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
