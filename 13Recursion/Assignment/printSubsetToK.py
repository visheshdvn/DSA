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
