# T = int(input())

# while T:
#     [X, Y] = [int(i) for i in input().split()]
#     if X+Y > 6:
#         print("YES")
#     else:
#         print("NO")
#     T -= 1

T = int(input())

while T:
    X, Y, Z = [int(i) for i in input().split()]
    print(X-Y, X-Y-Z)
    T -= 1
