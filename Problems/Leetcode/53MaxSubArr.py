from curses import curs_set


class Solution:
    def maxSubArray(self, nums):
        curr_max = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += n
            curr_max = max(curr_sum, curr_max)

        return curr_max


arr = [int(i) for i in input().split()]
ob = Solution()
print(ob.maxSubArray(arr))
