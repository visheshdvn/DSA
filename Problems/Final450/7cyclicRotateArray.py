def rotate(arr, k):
    arr = arr[k:] + arr[:k]


arr = [int(i) for i in input().split()]
k = int(input())
rotate(arr, k)
print(arr)
