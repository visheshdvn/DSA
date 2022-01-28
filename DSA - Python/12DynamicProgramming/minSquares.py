import math
import sys


def minSquares(n, dp):
    if n == 0:
        return 0
    
    ans = sys.maxsize
    root = int(math.sqrt(n))

    for i in range(1, root+1):

        newCheckVal = n-(i**2)
        if dp[newCheckVal] == -1:
            smallAns = minSquares(newCheckVal, dp)
            dp[newCheckVal] = smallAns
            currAns = 1+smallAns
        else:
            currAns = 1+dp[newCheckVal]

        ans = min(ans, currAns)

    return ans


n = int(input())
dp = [-1]*(n+1)
ans = minSquares(n, dp)
print(ans)
