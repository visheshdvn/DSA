class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        x = abs(x)
        revx = 0
        t = x

        while t != 0:
            revx = revx*10+t % 10
            t //= 10

        if isNegative:
            revx *= -1
            
        if revx > 2**31-1 or revx < -1*2**31:
            return 0

        return revx


x = int(input())
ob = Solution()
print(ob.reverse(x))
