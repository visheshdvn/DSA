import sys

def mcm(p, i, j, dp):

    if i == j:
        return 0

    min_val = sys.maxsize
    for k in range(i, j):
        if dp[i][k] == -1:
            ans1 = mcm(p, i, k, dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
            
        if dp[k+1][j] == -1:
            ans2 = mcm(p, k+1, j, dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]
    
        
        mCost = p[i-1]*p[k]*p[j]
        curr_val = ans1 + ans2 + mCost
        min_val = min(min_val, curr_val)
        
    return min_val


n = int(input())
p = [int(i) for i in input().split()]
dp = [[-1 for j in range(n+1)] for i in range(n+1)]

print(mcm(p, 1, n, dp))
