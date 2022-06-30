import sys

def minSteps(n):
    if n == 1:
        return 1
    
    ans1 = ans2 = ans3 = sys.maxsize
    
    ans1 = minSteps(n-1)
    
    if n&1 == 0:
        ans2 = minSteps(n//2)
    
    if n%3 == 0:
        ans3 = minSteps(n//3)
    
    return 1 + min(ans1, ans2, ans3)
    

# Main
sys.setrecursionlimit(100000)
n=int(input())
dp = [-1]*(n+1)
print(minSteps(n))
