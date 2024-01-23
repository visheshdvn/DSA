def LastIndex(arr, x, li):
    l = len(arr)
    if l == 0 or li == -l:
        return -1
    
    if arr[li] == x:
        return l + li
    
    return LastIndex(arr, x, li-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(LastIndex(arr, x, -1))