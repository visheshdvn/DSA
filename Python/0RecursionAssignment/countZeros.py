# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
def countzeros(n):
    if n == 0:
        return 0
    
    a = n % 10
    res = countzeros(n // 10)
    if a == 0:
        return 1 + res
    else:
        return res

n = int(input())
print(countzeros(n))