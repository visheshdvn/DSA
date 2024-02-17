def max_subarr_sum(arr):
    max_sum = arr[0]
    res = arr[0]

    for i in range(1, len(arr)):
        max_sum = max(arr[i], max_sum+arr[i])
        res = max(max_sum, res)

    return res


arr = [int(i) for i in input().split()]
print("Max subarray sum:", max_subarr_sum(arr))
