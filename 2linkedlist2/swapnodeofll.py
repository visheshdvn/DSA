class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    iterator1 = iterator2 = head

    while i >= 0:
        iterator1 = iterator1.next
        iterator2 = iterator2.next
        i -= 1
        j -= 1

    while j >= 0:
        iterator2 = iterator2.next 
        j -= 1

    # print(iterator1.data)
    # print(iterator2.data)
    iterator1.data, iterator2.data = iterator2.data, iterator1.data

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
i, j=list(int(i) for i in input().strip().split(' '))

if i>j:
    i, j = j, i

l = swap_nodes(l, i-1, j-1)
printll(l)
