# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midpoint_linkedlist(head):
    slow = fast = head

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

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
node = midpoint_linkedlist(l)
if node:
    print(node.data)
