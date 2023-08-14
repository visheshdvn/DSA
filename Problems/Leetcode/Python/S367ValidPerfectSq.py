def isPerfectSquare(num: int) -> bool:
    pos = 0
    while (num != 0):
        if ((num & 1) == 1):
            if ((pos & 1) != 0):
                return False
        num >>= 1
        pos += 1

    return True


n = int(input())
print(isPerfectSquare(n))

# 1001
# 1010001