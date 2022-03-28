def kthSmallestAndLargest(arr, k):
    arr.sort()
    return arr[k-1], arr[len(arr) - k]


arr = [int(i) for i in input().strip().split()]
k = int(input())
print(kthSmallestAndLargest(arr, k))
