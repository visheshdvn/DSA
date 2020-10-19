# Given an integer array (of length n), find and return all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :

# Line 1 : Size of array

# Line 2 : Array elements (separated by space)

# Sample Input:
# 3
# 15 20 12
# Sample Output:
# [] (this just represents an empty array, don't worry about the square brackets)
# 12 
# 20 
# 20 12 
# 15 
# 15 12 
# 15 20 
# 15 20 12 

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