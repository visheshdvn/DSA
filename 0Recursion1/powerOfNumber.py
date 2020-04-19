def powerOutput(x, n):
    if x == 1 or n == 0:
        return 1
    elif x == 0:
        return 0
    elif n == 1:
        return x
    else:
        return x * powerOutput(x, n-1)
    

x, n = list(map(int, input().split()))

output = powerOutput(x, n)
print(output)