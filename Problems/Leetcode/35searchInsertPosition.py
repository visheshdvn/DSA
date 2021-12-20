class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid

        if nums[mid] > target:
            return mid
        else:
            return mid + 1


nums = [int(i) for i in input().split()]
target = int(input())
ob = Solution()
print(ob.searchInsert(nums, target))
