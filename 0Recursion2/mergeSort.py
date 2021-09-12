def merge(arr, l, mid, r):
    n1 = mid-l+1
    n2 = r-mid

    lArr = arr[l:mid+1]
    rArr = arr[mid+1:r+1]

    i = 0
    j = 0
    k = l
    
    while i < n1 and j < n2:
        if lArr[i] < rArr[j]:
            arr[k] = lArr[i]
            i += 1
        elif lArr[i] > rArr[j]:
            arr[k] = rArr[j]
            j += 1
        else:
            arr[k] = lArr[i]
            i+=1
            k+=1
            arr[k] = rArr[j]
            j+=1
            k+=1
            continue
        k += 1

    while i < n1:
        arr[k] = lArr[i]
        i += 1
        k+=1

    while j < n2:
        arr[k] = rArr[j]
        j += 1
        k+=1


def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


        # Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, len(arr)-1)

for i in arr:
    print(i)
