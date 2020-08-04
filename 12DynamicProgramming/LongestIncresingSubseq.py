import sys
def lis(li, i, n):

    if i == n-1:
        return 0, 0

    including_max = 1
    for j in range(i+1, n):
        if  li[j] >= li[i]:
            
            ans = lis(li, j, n)
            further_including_max = ans[0]
                
            including_max = max(including_max, 1+ further_including_max)

    ans = lis(li, i+1, n)
    excluding_max = ans[1]

    overallMax = max(including_max, excluding_max)

    return including_max, overallMax

sys.setrecursionlimit(10000)
n = int(input())
li = [int(ele) for ele in input().split()]
ans = lis(li, 0, n)[1]
print(ans)
