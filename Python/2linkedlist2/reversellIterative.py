class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = head
    node = prev.next
    copy = None

    while node != None:
        prev.next = copy
        copy = prev
        prev = node
        node = node.next
    
    prev.next = copy
    return prev

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
l = reverse(l)
printll(l)
