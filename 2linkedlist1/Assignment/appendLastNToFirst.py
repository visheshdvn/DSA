class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n, lth):
    t = lth
    node = head
    while t:
        node = node.next
        t-=1

    node.next = head

    t = lth - (n % (lth+1))
    while t:
        head = head.next
        t-=1
    
    new_head = head.next
    head.next = None
    return new_head

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
i=int(input())
l = append_LinkedList(l, i, len(arr) - 2)
printll(l)
