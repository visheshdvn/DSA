def rearrange(arr):
    n = len(arr)
    j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            arr[i], arr[j] = arr[j], arr[i]
            j = j + 1

    return arr


arr = [int(i) for i in input().strip().split()]
rearrange(arr)
print(*arr)
