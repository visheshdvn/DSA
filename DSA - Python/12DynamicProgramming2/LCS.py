# Given two strings S1 and S2 with lengths M and N respectively, find the length of the longest common subsequence.
# A subsequence of a string S whose length is K, is a string containing characters in same relative order as they are present in S, but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K. For example, subsequences of string "abc" are -- ""(empty string), a, b, c, ab, bc, ac, abc.
# Input Format :
# Line 1: String S1
# Line 2: String s2
# Output Format :
# Length of the longest common subsequence.
# Constraints :
# 1 <= M <= 100
# 1 <= N <= 100

# Time Limit: 1 sec
# Sample Input 1:
# adebc
# dcadb
# Sample Output 1:
# 3
# Explanation of Sample Input 1:
# "a", "d", "b", "c", "ad", "ab", "db", "dc" and "adb" are present as a subsequence in both the strings in which "adb" has the maximum length. There are no other common subsequence of length greater than 3 and hence the answer.
# Sample Input 2:
# abcd
# acbdef
# Sample Output 2:
# 3
# Explanation of Sample Input 2:
# "a", "b", "c", "d", "ab", "ac", "ad", "bd", "cd", "abd" and "acd" are present as a subsequence in both the strings S1 and S2 in which "abd" and "acd" are of the maximum length. There are no other common subsequence of length greater than 3 and hence the answer.

def lcs(str1, str2, i, j, dp):
    if i == len(str1) or j == len(str2):
        return 0
    
    if str1[i] == str2[j]:
        if dp[i+1][j+1] == -1:
            ans = 1+ lcs(str1, str2, i+1, j+1, dp)
            dp[i+1][j+1] = ans -1
        else:
            ans = 1 + dp[i+1][j+1]
    else:
        if dp[i+1][j] == -1:
            ans1 = lcs(str1, str2, i+1, j, dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]
        
        
        if dp[i][j+1]:
            ans2 = lcs(str1, str2, i, j+1, dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]
            
        ans = max(ans1, ans2)
    
    return ans


str1 = input()
str2 = input()

n = len(str1)
m = len(str2)
dp = [[-1 for j in range(m+1)] for i in range(n+1)]

ans = lcs(str1, str2, 0, 0, dp)
print(ans)
 