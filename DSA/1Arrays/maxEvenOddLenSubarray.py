def max_alt_subarray(arr):
    if len(arr) == 0:
        return 0

    max_count = 0
    count = 0
    expectation = arr[0] & 1

    for i in arr:
        if (i & 1) != expectation:
            count = 1
        else:
            count += 1
            expectation = 1 - expectation

        max_count = max(count, max_count)

    return max_count


arr = [int(i) for i in input().split()]
print("Max alt subarray:", max_alt_subarray(arr))
