from typing import List


def bubbleSort(arr: List[int]) -> None:
    n = len(arr)-1

    while(n):
        j = 0
        while (j < n):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        n -= 1


arr = [int(i) for i in input().split()]
bubbleSort(arr)
print(*arr)
