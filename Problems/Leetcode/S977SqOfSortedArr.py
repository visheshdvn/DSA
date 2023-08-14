class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i]**2
    
        return sorted(nums)
    
arr = [int(i) for i in input().split()]
ob = Solution()
print(ob.sortedSquares(arr))