def reverseArray(a):
    n = len(a)
    for i in range(0, len(a)//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

arr = [int(i) for i in input().strip().split(' ')]
reverseArray(arr)
print(*arr)
