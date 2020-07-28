import sys, math

def minStepsTo1(n, dp):
    if n == 0:
        return 0

    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        
        newCheckValue = n-(i**2)
        if dp[newCheckValue] == -1:
            dp[newCheckValue] = 1 + minStepsTo1(n-(i**2), dp)
            currAns = dp[newCheckValue] + 1
        else:
            currAns = dp[newCheckValue]
             
        ans = min(ans, currAns)

    return ans

sys.setrecursionlimit(10000)
n = int(input())
dp = [-1]*(n+1)
ans = minStepsTo1(n, dp)
print(ans)