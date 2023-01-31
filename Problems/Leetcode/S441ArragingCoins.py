from math import sqrt


def arrangeCoins(n: int) -> int:
    n = (-1 + sqrt(1 + 8*n))//2
    return int(n)

n = int(input())
print(arrangeCoins(n))

# n^2 +n -2s
