import sys

def minCostPath(i, j, m, n, mat, dp):
    if i == m-1 and j == n-1:
        return mat[i][j]
    
    a, b, c = 99999, 99999, 99999
    
    
    if i < m-1:
        if dp[i+1][j] == sys.maxsize:
            a = minCostPath(i+1, j, m, n, mat, dp)
            dp[i+1][j] = a
        else:
            a = dp[i+1][j]
    
    if i < m-1 and j < n-1:
        if dp[i+1][j+1] == sys.maxsize:
            b = minCostPath(i+1, j+1, m, n, mat, dp)
            dp[i+1][j+1] = b
        else:
            b = dp[i+1][j+1]
    
    if j < n-1:
        if dp[i][j+1] == sys.maxsize:
            c = minCostPath(i, j+1, m, n, mat, dp)
            dp[i][j+1] = c
        else:
            c = dp[i][j+1]
    
    
    return mat[i][j] + min([a, b, c])
     

m, n = [int(i) for i in input().strip().split()]
mat = []

for i in range(m):
    lst = [int(i) for i in input().split()]
    mat.append(lst)

dp = [[sys.maxsize for i in range(m+1)] for i in range(n+1)]

ans = minCostPath(0, 0, m, n, mat, dp)
print(ans)
