class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check_palindrome(head) :
    elements = []
    index = -1

    while head != None:
        elements.append(head.data)
        head = head.next
    
    if elements == elements[::-1]:
        return True
    else:
        return False


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
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
