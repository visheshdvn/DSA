class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        profit = 0
        curr_min = float("inf")
        curr_max = 0

        for i in prices:
            if i < curr_min:
                curr_min = i
                curr_max = 0
                continue

            if i > curr_max:
                curr_max = i
                profit = max(profit, curr_max-curr_min)
        
        return profit


arr = [int(i) for i in input().split()]
ob = Solution()
print(ob.maxProfit(arr))
