def firstIndex(arr, x, fi):
    if fi == len(arr):
        return -1
    
    if arr[fi] == x:
        return fi
        
    return firstIndex(arr, x, fi+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

print("Enter elements of Array: ")
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())

print(firstIndex(arr, x, 0))