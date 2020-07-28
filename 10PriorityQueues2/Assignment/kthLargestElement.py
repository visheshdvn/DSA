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