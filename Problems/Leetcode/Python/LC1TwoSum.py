# assumption: ony one valid pair exist

def get_sum_pair(nums, target):
    ans = []
    pos = {}
    
    for i in range(len(nums)):
        if pos.get(target - nums[i], -1) == -1:
            pos[nums[i]] = i
        else:
            return [pos[target - nums[i]], i]
    
    return ans


print("Enter array nums:", end=" ")
nums = [int(i) for i in input().strip().split()]
n = int(input("Enter the target value: "))

print("Pair: ", get_sum_pair(nums, n))