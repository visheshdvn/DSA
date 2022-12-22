class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete(head, i, n):
    if i < 0 or i >= n:
        return head

    prev = None
    current = head

    if i == 0:
        head = head.next
        return head

    while i:
        prev = current
        current = current.next
        i -= 1

    if current.next == None:
        prev.next = None
    else:
        current = current.next
        prev.next = current

    return head


def ll(arr):
    if len(arr) == 0:
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
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
n = len(arr)
l = ll(arr[:-1])
i = int(input())
l = delete(l, i, n-1)
printll(l)
