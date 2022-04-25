def n_pairs(arr, n, target):
    low = 0
    high = n-1
    count = 0

    while low < high:
        if arr[low] + arr[high] > target:
            high -= 1
        elif arr[low] + arr[high] < target:
            low += 1
        else:
            count += 1
            low += 1
            high -= 1

    if count:
        return count

    return -1


arr = [int(i) for i in input().strip().split()]
target = int(input())
print(n_pairs(arr, len(arr), target))
