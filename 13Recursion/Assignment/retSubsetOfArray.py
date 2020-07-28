def subsetArr(arr):
    if len(arr) == 1:
        return [arr]
    
    a = arr[0]
    lst = subsetArr(arr[1:])
    
    ret_lst = [[a]]
    
    for i in lst:
        array = i[:]
        array.insert(0, a)
        ret_lst.append(array)
        
    return lst+ret_lst

    
n = int(input())
arr = [int(element) for element in list(input().strip().split(" "))]
ans = subsetArr(arr)
for i in ans:
    for j in i:
        print(j, end=" ")
    print()