def intersection(n1, n2, arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    # arr3 = []
    i = j = 0
    
    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            print(arr1[i])
            i += 1
            j += 1
            continue
        
        if arr1[i] > arr2[j]:
            j += 1
            continue
        else:
            i += 1
    
    # print(arr3)

# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(n1, n2, arr1, arr2) 
