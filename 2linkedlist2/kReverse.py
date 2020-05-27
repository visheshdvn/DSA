class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    if head == None or head.next == None:
        return [head, head]

    node = head.next
    head.next = None

    tail, nhead = reverse(node)

    tail.next = head
    return [head, nhead]


def kReverse(head, n):
    if n == 1:
        return [None, head]

    node = head
    i = n-1
    while i:
        if node == None or node.next == None:
            return reverse(head)
        node = node.next
        i -=1

    
    new_node = node.next
    node.next = None

    a, b = reverse(head)
    tail, head = kReverse(new_node, n)

    a.next = head

    return [tail, b]


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
# printll(l)
tail, head = kReverse(l, i)
printll(head)
