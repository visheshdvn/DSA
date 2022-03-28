def reverseArrayAfterM(a, m):
    l = m+1
    r = len(a)-1

    while (l <= r):
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1


arr = [int(i) for i in input().strip().split(' ')]
m = int(input())
reverseArrayAfterM(arr, m)
print(*arr)
