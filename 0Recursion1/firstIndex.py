def firstIndex(arr, x, fi):
    if fi == len(arr):
        return -1
    if arr[fi] == x:
        return fi
        
    return 0 + firstIndex(arr, x, fi+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, 0))



# Copying list way
# def firstIndex(a, x):
#     l = len(a)
#     if l == 0:
#         return -1
    
#     if a[0] == x:
#         return 0
#     smallerListOutput = firstIndex(a[1:], x)
    
#     if smallerListOutput == -1:
#         return -1
#     else:
#         return smallerListOutput + 1