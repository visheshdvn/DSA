def printAllSubsetsRec(arr, n, v, sum) : 
    
    if (sum == 0) : 
        for value in v : 
            print(value, end=" ") 
        print() 
        return

    if (n == 0): 
        return
    
    printAllSubsetsRec(arr, n - 1, v, sum)
    v1 = [] + v
    v1.insert(0, arr[n - 1])
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1])


# Wrapper over printAllSubsetsRec()
def printAllSubsets(arr, n, sum):
    v = []
    printAllSubsetsRec(arr, n, v, sum)


# Driver code
n = int(input())
arr = [int(element) for element in list(input().strip().split(" "))]
sum = int(input())
printAllSubsets(arr, n, sum)