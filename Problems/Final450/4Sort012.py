def Sort012(arr, n):
    if n == 1:
        return

    i, j, k = 0, 0, n-1

    while j <= k:
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] == 1:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1


arr = [int(i) for i in input().strip().split()]
Sort012(arr, len(arr))
print(arr)
