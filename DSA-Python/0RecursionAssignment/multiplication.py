def multiplication(x, y):
    if x == 0 or y == 0:
        return 0
    
    return x + multiplication(x, y-1)

a = int(input())
b = int(input())
if a > b:
    print(multiplication(a, b))
else:
    print(multiplication(b, a))