import heapq
def kSmallest(lst, k):
    heap = lst[0:k]
    heapq.heapify(heap)
    
    for i in lst[k:]:
        if i > heap[0]:
            heapq.heapreplace(heap, i)
            
    return heap

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans = kSmallest(lst, k)
ans.sort()
for i in ans:
    print(i)
