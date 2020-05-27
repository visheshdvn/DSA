def power(x, n):
    if n == 0:
        return 1
    num = power(x, n//2); 
    if n%2 == 0:
        return num*num; 
    else:
        return x*num*num; 
    
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
