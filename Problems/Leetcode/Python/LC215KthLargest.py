from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    level = 0
    largest = float("-inf")


arr = [int(i) for i in input().split()]
k = int(input())
print(findKthLargest(arr, k))
