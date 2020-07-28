def subsetArr(arr, lst):
    if arr == []:
        for i in lst:
            for j in i:
                print(j, end=' ')
            print()
        return
    
    a = arr.pop(0)
    
    payload = []
    
    for i in lst:
        array = i[:]
        array.append(a)
        payload.append(array)
    
    subsetArr(arr, lst+payload)

    
n = int(input())
arr = [int(element) for element in list(input().strip().split(" "))]
subsetArr(arr, [[]])


# 15 
# 20 
# 15 20 

# 12 
# 15 12 
# 20 12
# 15 20 12 
