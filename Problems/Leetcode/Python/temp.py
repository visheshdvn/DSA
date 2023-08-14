def tempFunc(mat, k):
    # Approach 1
    temp = []
    for i, m in enumerate(mat):
        # since it has only 1 and 0, the total sum will be total 1s.
        sol = (sum(m), i)
        temp.append(sol)
    print("temp before", temp)
    temp.sort()
    print("temp after", temp)
    return 0


rows = int(input())
mat = [[int(j) for j in input().split()] for _ in range(rows)]
k = int(input())
print(tempFunc(mat, k))
