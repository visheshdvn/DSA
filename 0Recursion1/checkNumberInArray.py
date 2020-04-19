def checkNumber(arr, x, n):
    if n == 0:
        return False or (x == arr[n])
    
    if x == arr[n]:
        return True
    
    return False or checkNumber(arr, x, n-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x, n-1):
    print('true')
else:
    print('false')
