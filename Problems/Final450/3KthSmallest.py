def kthSmallest(arr, k):
    arr.sort()
    return arr[k-1]


arr = [int(i) for i in input().strip().split()]
k = int(input())
print(kthSmallest(arr, k))
