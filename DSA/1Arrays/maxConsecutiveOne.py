def max_consecutive_ones(arr):
    max_ones = 0
    count = 0

    for i in arr:
        if i == 1:
            count += 1
            max_ones = max(max_ones, count)
        else:
            count = 0

    return max_ones


arr = [int(i) for i in input().split()]
print("Max Consecutive one:", max_consecutive_ones(arr))
