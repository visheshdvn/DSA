def staircase(init, num, n):
    if init + num > n:
        return 0

    if init + num == n:
        return 1
    
    a = staircase(init + num, 1, n)
    b = staircase(init + num, 2, n)
    c = staircase(init + num, 3, n)
    
    return a + b + c

n = int(input())
print(staircase(0, 1, n))