def MinDiff(A, K):
    A.sort()
    
    if A[-1] - A[0] > K:
        return

A = [int(i) for i in input().split()]
K = int(input())
print(MinDiff(A, K))