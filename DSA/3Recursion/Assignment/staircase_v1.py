# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.

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
