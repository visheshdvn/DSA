def maxMinEle(arr):
    max_ele = float('-inf')
    min_ele = float('inf')

    for i in range(len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]

        if arr[i] < min_ele:
            min_ele = arr[i]

    return max_ele, min_ele


arr = [int(i) for i in input().strip().split(' ')]
print(f"Max and min element respectively: {maxMinEle(arr)}")
