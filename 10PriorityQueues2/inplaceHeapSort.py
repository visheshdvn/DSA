def down_heapify(arr, i, n):
    pIndex = i
    lcIndex = 2 * pIndex + 1
    rcIndex = 2 * pIndex + 2
    
    while lcIndex < n:
        minIndex = pIndex
        if arr[minIndex] > arr[lcIndex]:
            minIndex = lcIndex
        
        if rcIndex < n and arr[minIndex] > arr[rcIndex]:
            minIndex = rcIndex
        
        if minIndex == pIndex:
            return
        
        arr[minIndex], arr[pIndex] = arr[pIndex], arr[minIndex]
        pIndex = minIndex
        lcIndex = 2*pIndex+1
        rcIndex = 2*pIndex+2

    
def heapSort(n, arr):
    
    for i in range(n//2, -1, -1):
        down_heapify(arr, i, n)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heapify(arr, 0, i)
        

n = int(input())
arr = [int(ele) for ele in input().strip().split()]
heapSort(n, arr)

print(*arr)