class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMiddle(head): 
    if (head == None): 
        return head 

    slow = head 
    fast = head 

    while (fast.next != None and fast.next.next != None): 
        slow = slow.next
        fast = fast.next.next
            
    return slow

def mergeSort(head):
    # Base case if head is None 
    if head == None or head.next == None: 
        return head 

    mid = getMiddle(head) 
    nextmid = mid.next
    mid.next = None
 
    left = mergeSort(head) 
    right = mergeSort(nextmid) 

    sortedl = sortedMerge(left, right) 
    return sortedl


def sortedMerge(left, right): 
    if left == None:
        return right 
    if right == None:
        return left
        
    result = None
            
    if left.data <= right.data: 
        result = left 
        result.next = sortedMerge(left.next, right) 
    else: 
        result = right 
        result.next = sortedMerge(left, right.next) 
    return result 


def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)
