# find max value of arr[j] - arr[i], j > i

def max_diff(arr):
    if len(arr) == 1:
        return arr[0]

    min_elem = arr[0]
    diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        diff = max(diff, arr[i] - min_elem)
        min_elem = min(min_elem, arr[i])

    return diff


arr = [int(i) for i in input().split()]
print("Max difference:", max_diff(arr))
