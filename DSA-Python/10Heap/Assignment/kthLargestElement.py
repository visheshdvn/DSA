# Given an array A of random integers and an integer k, find and return the kth largest element in the array.
# Try to do this question in less than O(nlogn) time.
# Input Format :
# Line 1 : An integer N i.e. size of the array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : An integer k
# Output Format :
# kth largest element
# Input Constraints :
# 1 <= N, Ai, k <= 10^5
# Sample Input 1 :
# 6
# 9 4 8 7 11 3
# 2
# Sample Output 1 :
# 9
# Sample Input 2 :
# 8
# 2 6 10 11 13 4 1 20
# 4
# Sample Output 2 :
# 10


import heapq
def kthLargest(lst, k):
    
    heap = lst[0:k]
    heapq.heapify(heap)
    
    for i in lst[k:]:
        if i > heap[0]:
            heapq.heapreplace(heap, i)
    
    # print(heap)
    return heap[0]


# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)