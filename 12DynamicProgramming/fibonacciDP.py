def Fibonacci(n, dp):
    if n <= 0 or n == 1:
        return n
    elif n == 2:
        return 1

    if dp[n-1] == -1:
        ans1 = Fibonacci(n-1, dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]

    if dp[n-2] == -1:
        ans2 = Fibonacci(n-2, dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]

    return ans1 + ans2


n = int(input())
dp = [-1]*(n+1)
print(Fibonacci(n, dp))
