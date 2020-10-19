# Problem ID 331 even after odd in a LL
# Arrange elements in a given Linked List such that, all even numbers are placed after odd numbers. Respective order of elements should remain same.
# Note: Input and Output has already managed for you. You don't need to print the elements, instead return the head of updated LL.
# Input format:
# Linked list elements (separated by space and terminated by -1)
# Output format:
# Print the elements of updated Linked list. 
# Sample Input 1 :
# 1 4 5 2 -1
# Sample Output 1 :
# 1 5 4 2 
# Sample Input 2 :
# 1 11 3 6 8 0 9 -1
# Sample Output 2 :
# 1 11 3 9 6 8 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createNodeandReturn(a):
    node = Node(a)
    return node

def arrange_LinkedList(head):
    evenList = Node(0)
    ehead = evenList
    oddList = Node(0)
    rhead = oddList
    node = head

    while node != None:
        if node.data & 1:
            oddList.next = createNodeandReturn(node.data)
            oddList = oddList.next
        else:
            evenList.next = createNodeandReturn(node.data)
            evenList = evenList.next

        node = node.next

    ehead = ehead.next
    oddList.next = ehead

    return rhead.next


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
l = arrange_LinkedList(l)
printll(l)
