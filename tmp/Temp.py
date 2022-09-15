def reverseBits(n):
    rev_str = ""
    bits = 0
    while n:
        rev_str += str(n & 1)
        n = n >> 1
        bits += 1

    rev_str += "0"*(32-bits)
    return int(rev_str, 2)


n = int(input())
print(reverseBits(n))

# 1010
