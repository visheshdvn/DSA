def binarySearch(a, x, si, ei):
    if si > ei:
        return -1
    
    mid = (si+ei)//2
    
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binarySearch(a, x, si, mid -1)
    else:
        return binarySearch(a, x, mid+1, ei)
    
elements = list(int(x) for x in input().strip().split(' '))
elements = list(int(i) for i in input().strip().split(' '))
element_to_search = int(input())
print(binarySearch(elements, element_to_search, 0, len(elements) -1))