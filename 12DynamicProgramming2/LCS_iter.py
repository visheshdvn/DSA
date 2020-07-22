def lcs(str1, str2):
    
    n = len(str1)
    m = len(str2)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            
            if str1[i] == str2[j]:
                dp[i][j] = 1+ dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
    return dp[0][0]


str1 = input()
str2 = input()
ans = lcs(str1, str2)
print(ans)