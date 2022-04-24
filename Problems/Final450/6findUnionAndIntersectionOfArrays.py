def getUnionAndIntersectionCount(A, B):
    A.sort()
    B.sort()
    nA = len(A)
    nB = len(B)
    countIntersection = 0

    i = 0
    j = 0

    while i < nA and j < nB:
        if A[i] == B[j]:
            countIntersection += 1
            i += 1
            j += 1
            continue

        if A[i] > B[j]:
            j += 1
            continue

        if B[j] > A[i]:
            i += 1
            continue

    return countIntersection, nA+nB-countIntersection


A = [int(i) for i in input().strip().split()]
B = [int(i) for i in input().strip().split()]

print(getUnionAndIntersectionCount(A, B))
