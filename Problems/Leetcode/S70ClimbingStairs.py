from locale import currency


class Solution:
    def climbStairsHelper(self, n, currStep):
        if currStep > n:
            return 0

        if currStep == n:
            return 1

        step1 = self.climbStairsHelper(n, currStep+1)
        step2 = self.climbStairsHelper(n, currStep+2)

        return step1 + step2

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        return self.climbStairsHelper(n, 0)


n = int(input())
ob = Solution()
steps = ob.climbStairs(n)
print(steps)

1 1 1 1
1 1 2
1 2 1
2 2
2 1 1