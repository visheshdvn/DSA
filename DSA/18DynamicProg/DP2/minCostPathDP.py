# Given an integer matrix of size m*n, you need to find out the value of minimum cost to reach from the cell (0, 0) to (m-1, n-1).
# From a cell (i, j), you can move in three directions : (i+1, j), (i, j+1) and (i+1, j+1).
# Cost of a path is defined as the sum of values of each cell through which path passes.
# Input Format :
# Line 1 : Two integers, m and n
# Next m lines : n integers of each row (separated by space)
# Output Format :
# Minimum cost
# Constraints :
# 1 <= m, n <= 20
# Sample Input 1 :
# 3 4
# 3 4 1 2
# 2 1 8 9
# 4 7 8 1
# Sample Output 1 :
# 13

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
