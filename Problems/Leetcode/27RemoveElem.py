def removeElement(nums, val):
    curr = 0
    n = 0

    while n < len(nums):
        if nums[n] == val:
            n += 1
        elif nums[n] != val:
            nums[curr] = nums[n]
            curr += 1
            n += 1
    
    return curr


n = int(input())
arr = [int(i) for i in input().split()]

i = removeElement(arr, n)
print(arr[:i])
