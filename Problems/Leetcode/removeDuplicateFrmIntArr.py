class Solution:
    def removeDuplicates(self, nums):
        ind = 0
        
        for i in range(1, len(nums)):
            if nums[ind] != nums[i]:
                ind += 1
                continue
            
            


x = [int(i) for i in input().strip().split()]
ob = Solution()
ob.removeDuplicates(x)
print(x)
