class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linearSearch(head, n):

    i = 0
    while head != None and head.data != n:
        i += 1
        head = head.next

    if head == None:
        return -1
    return i

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
data=int(input())
index = linearSearch(l, data)
print(index)
