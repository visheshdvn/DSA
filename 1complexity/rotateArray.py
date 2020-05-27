
def rotate(arr, d):
    while d:
        arr.append(arr.pop(0))
        d -= 1


def takeInput() :
    n = int(input().strip())
    if n != 0:
        arr = [int(element) for element in list(input().strip().split())]
        return arr, n

    return list(), 0



def printList(arr) : 
	for element in arr :
		print(element, end = " ")
	print()


#main
arr, n = takeInput()
d = int(input().strip())

rotate(arr, d)
printList(arr)