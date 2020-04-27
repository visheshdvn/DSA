def geometricSum(n):
    if n == 0:
        return 1
    
    return 1/(2**n) + geometricSum(n-1)
    
n = int(input())
ans = geometricSum(n)
print('%.5f'%ans)