# Given a positive integer n, find the minimum number of steps s, that takes n to 1. You can perform any one of the following 3 steps.
# 1.) Subtract 1 from it. (n= n - ­1) ,
# 2.) If its divisible by 2, divide by 2.( if n%2==0, then n= n/2 ) ,
# 3.) If its divisible by 3, divide by 3. (if n%3 == 0, then n = n / 3 ). 
# The time complexity of your code should be O(n).
# Input format :
# Line 1 : A single integer i.e. n
# Output format :
# Line 1 : Single integer i.e number of steps
# Constraints :
# 1 <= n <= 10^5
# Sample Input 1 :
# 4
# Sample Output 1 :
# 2 
# Sample Output 1 Explanation :
# For n = 4
# Step 1 : n = 4/2 = 2
# Step 2 : n = 2/2 = 1
# Sample Input 2 :
# 7
# Sample Output 2 :
# 3
# Sample Output 2 Explanation :
# For n = 7
# Step 1 : n = 7 ­ - 1 = 6
# Step 2 : n = 6 / 3 = 2
# Step 3 : n = 2 / 2 = 1

import sys

def minStepsTo1DP(n, dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    if n == 1:
        return 0
    
    ans1 = sys.maxsize
    if n%3 == 0:
        if dp[n//3] == -1:
            ans1 = minStepsTo1DP(n//3, dp)
            dp[n//3] = ans1
        else:
            ans1 = dp[n//3]
        
        
    ans2 = sys.maxsize
    if n%2 == 0:
        if dp[n//2] == -1:
            ans2 = minStepsTo1DP(n//2, dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]
    
    if dp[n-1] == -1:
        ans3 = minStepsTo1DP(n-1, dp)
        dp[n-1] = ans3
    else:
        ans3 = dp[n-1]
    
    ans = 1 + min(ans1, ans2, ans3)
    return ans        
    

# Main
sys.setrecursionlimit(100000)
n=int(input())
dp = [-1]*(n+1)
print(minStepsTo1DP(n, dp))
