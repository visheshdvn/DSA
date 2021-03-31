class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubbleSortLL(head, n):
    for i in range(n):
        node1 = head
        node2 = head.next

        for j in range(n-1-i):
            if node1.data > node2.data:
                node1.data, node2.data = node2.data, node1.data
            node1 = node1.next
            node2 = node2.next

    return head

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
l = bubbleSortLL(l, len(arr)-1)
printll(l)
