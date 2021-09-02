class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def append_LinkedList(head, n, l):
    fwd = l-n-1
    temp = head

    while fwd:
        temp = temp.next
        fwd -= 1

    new_head = temp.next
    temp.next = None

    node = new_head
    while node.next:
        node = node.next

    node.next = head
    return new_head


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    itr = head
    for i in arr[1:]:
        itr.next = Node(i)
        itr = itr.next
    return head


def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i = int(input())
l = append_LinkedList(l, i, len(arr)-1)
printll(l)
