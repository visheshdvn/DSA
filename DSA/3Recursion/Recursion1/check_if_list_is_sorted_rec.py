def check_if_list_is_sorted_asc(arr, i=0):
    if len(arr) == 0 or len(arr) == 1 or i >= len(arr)-1:
        return True
    
    if (arr[i] > arr[i+1]):
        return False
    
    return check_if_list_is_sorted_asc(arr, i+1)


arr = [int(i) for i in input().strip().split()]
print(check_if_list_is_sorted_asc(arr))