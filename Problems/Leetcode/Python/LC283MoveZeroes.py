def move_zeroes(nums):
    curr = 0
    n = 0

    while n < len(nums):
        if nums[n] != 0:
            nums[curr] = nums[n]
            curr += 1
        n += 1

    while curr < len(nums):
        nums[curr] = 0
        curr += 1


arr = [int(i) for i in input().split()]

move_zeroes(arr)
print(arr)
