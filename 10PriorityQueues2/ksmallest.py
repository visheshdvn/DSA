import heapq
def kSmallest(lst, k):
    heap = lst[0:k]
    heapq._heapify_max(heap)
    
    for i in lst[k:]:
        if i < heap[0]:
            heapq._heapreplace_max(heap, i)
            
    return heap

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans = kSmallest(lst, k)
ans.sort(reverse=True)
for i in ans:
    print(i)
