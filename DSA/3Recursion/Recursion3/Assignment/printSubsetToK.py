# Given an array A and an integer K, print all subsets of A which sum to K.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important. Just print them in different lines.
# Input format :
# Line 1 : Size of input array
# Line 2 : Array elements separated by space
# Line 3 : K 
# Sample Input:
# 9 
# 5 12 3 17 1 18 15 3 17 
# 6
# Sample Output:
# 3 3
# 5 1

import sys
sys.setrecursionlimit(10 ** 8)


def subsetsSumK(arr, k, values):
    if len(arr) == 0:
        for i in values:
            for j in i:
                print(j, end=" ")
            print()
        return
    
    a = arr[0]
    
    if k-a in arr[1:]:
        values.append([a, k-a])
        
    if a == k:
        values.append([a])
        
    subsetsSumK(arr[1:], k, values)
    
#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    subsetsSumK(arr, k, [])
