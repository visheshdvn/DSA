def remove_dupl(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return 1
    
    count = 1;
    i = 0
    j = 1
    
    while j < len(arr):
        if arr[j] != arr[i]:
            i+=1
            arr[i] = arr[j]
            count+=1
        j+=1
    
    return count
    


print("Enter sorted array:", end=" ")
arr = [int(i) for i in input().strip().split()]
size = remove_dupl(arr)

i = 0
while i < size:
    print(arr[i], end=" ")
    i+=1
