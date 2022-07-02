from ast import Num
from typing import List


def insertionSort(arr: List[int]) -> None:
    if len(arr) == 1:
        return

    for i in range(1, len(arr)):
        j = i-1
        num = arr[i]
        while j >= 0 and (num < arr[j]):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = num


arr = [int(i) for i in input().split()]
insertionSort(arr)
print(*arr)
