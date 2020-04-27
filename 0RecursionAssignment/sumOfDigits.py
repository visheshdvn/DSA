def sumofdigits(n):
    if n // 10 == 0:
        return n
    
    return n%10 + sumofdigits(n // 10)
    
n = int(input())
print(sumofdigits(n))