import sys
sys.setrecursionlimit(10 ** 8)


def subsetsSumK(arr, k):
    if len(arr) == 1:
        return arr, []
    
    num = arr[0]
    o, ret = subsetsSumK(arr[1:], k)
    
    if k-num in o:
        ret.append([num, k-num])
    
    return arr, ret
        
    
#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    garbage, liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)
