# Check Max-Heap
# Send Feedback
# Given an array of integers, check whether it represents max-heap or not.
# Return true or false.
# Input Format :
# Line 1 : An integer N i.e. size of the array
# Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :
# true if it represents max-heap and false if it is not a max-heap
# Constraints :
# 1 <= N <= 10^5
# 1 <= Ai <= 10^5

import heapq
def checkMaxHeap(lst, n):
    pIndex = n
    lcIndex = 2 * pIndex + 1
    rcIndex = 2 * pIndex + 2
    
    if lcIndex >= len(lst):
        return True
    
    if rcIndex >= len(lst):
        if lst[pIndex] < lst[lcIndex]:
            return False
        else:
            return True
    
    if rcIndex < len(lst):
        if lst[pIndex] < lst[lcIndex] or lst[pIndex] < lst[rcIndex]:
            return False
    
    
    truth1 = True and checkMaxHeap(lst, lcIndex)
    truth2 = True and checkMaxHeap(lst, rcIndex)
    
    return truth1 and truth2
    
# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split())
print('true') if checkMaxHeap(lst, 0) else print('false')
