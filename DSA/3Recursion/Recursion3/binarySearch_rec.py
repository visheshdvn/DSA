def binary_search_helper(arr, l, h, n):
    if h < l:
        return -1
    
    mid = (l + h)//2
    
    if n == arr[mid]:
        return mid
    elif (n < arr[mid]):
        return binary_search_helper(arr, l, mid-1, n)
    else:
        return binary_search_helper(arr, mid+1, h, n)
    

def binary_search(arr, n):
    return binary_search_helper(arr, 0, len(arr)-1, n)


print("Enter array numbers:", end=" ")
arr = [int(i) for i in input().strip().split()]
n = int(input("Enter number to search: "))
print(binary_search(arr, n))