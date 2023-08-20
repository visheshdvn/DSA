from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = -1*abs(nums[abs(num)-1])

        disappared = []
        for i in range(len(nums)):
            if nums[i] > 0:
                disappared.append(i+1)

        return disappared


arr = [int(i) for i in input().split()]
ob = Solution()
print(*ob.findDisappearedNumbers(arr))
