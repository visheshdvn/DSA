def FindUnique(n, arr):
    arr.sort()
    i = 0
    
    while i <= n:
        if i == n-1 or arr[i] != arr[i+1]:
            return arr[i]
        
        i+=2

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(n, arr)
print(unique)
