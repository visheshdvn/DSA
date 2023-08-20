from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        first = second = third = float("-inf")

        for i in nums:
            if i > first:
                third = second
                second = first
                first = i
            elif second < i < first:
                third = second
                second = i
            elif third < i < second:
                third = i

        if third == float("-inf"):
            return first
        
        return third


arr = [int(i) for i in input().split()]
ob = Solution()
print(ob.thirdMax(arr))
