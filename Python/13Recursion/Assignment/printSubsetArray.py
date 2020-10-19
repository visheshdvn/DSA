# Print Subsets of Array
# Given an integer array (of length n), find and print all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important. Just print the subsets in different lines.
# Input format :
# Line 1 : Integer n, Size of array
# Line 2 : Array elements (separated by space)
# Constraints :
# 1 <= n <= 15
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
