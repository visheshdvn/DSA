def minCostPath(i, j, m, n, mat):
    if i == m-1 and j == n-1:
        return mat[i][j]
    
    a, b, c = 99999, 99999, 99999
    
    if i < m-1:
        a = minCostPath(i+1, j, m, n, mat)
    
    if i < m-1 and j < n-1:
        b = minCostPath(i+1, j+1, m, n, mat)
    
    if j < n-1:
        c = minCostPath(i, j+1, m, n, mat)
    
    
    
    return mat[i][j] + min([a, b, c])
    

m, n = [int(i) for i in input().strip().split()]
mat = []

for i in range(m):
    lst = [int(i) for i in input().split()]
    mat.append(lst)

ans = minCostPath(0, 0, m, n, mat)
print(ans)
