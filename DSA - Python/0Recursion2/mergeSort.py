# Complexity -
# Best Case Time Complexity: O(n*log n)
# Worst Case Time Complexity: O(n*log n)
# Average Time Complexity: O(n*log n)

# CODE -

def merge(arr, l, mid, r):
    n1 = mid-l+1  # Number of elements in left subarray
    n2 = r-mid    # Number of elements in right subarray

    lArr = arr[l:mid+1]  # Left subarray
    rArr = arr[mid+1:r+1]  # Right subarray

    i = 0  # Index for left subarray
    j = 0  # Index for right subarray
    k = l  # Index for merged subarray

    while i < n1 and j < n2:  # While both subarrays are not empty
        if lArr[i] < rArr[j]:
            arr[k] = lArr[i]
            i += 1
        elif lArr[i] > rArr[j]:
            arr[k] = rArr[j]
            j += 1
        else:
            arr[k] = lArr[i]
            i += 1
            k += 1
            arr[k] = rArr[j]
            j += 1
            k += 1
            continue
        k += 1

    while i < n1:
        arr[k] = lArr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = rArr[j]
        j += 1
        k += 1


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
