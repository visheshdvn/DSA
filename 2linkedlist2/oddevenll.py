# Problem ID 331 even after odd in a LL
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
