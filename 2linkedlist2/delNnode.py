class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    if M == N == 0:
        return None

    if N == 0:
        return head

    if M == 0 and N != 0:
        return None
        
    nhead = Node(0)
    nhead.next = head
    dl = N - 1
    skip = M
    node = nhead

    while skip:
        if node == None:
            return head
        node = node.next
        skip -= 1

    if node == None:
        return head

    skipped = node.next
    node.next = None

    while dl:
        if skipped == None:
            return head
        skipped = skipped.next
        dl -= 1
    
    if skipped == None:
        return head
    
    smallhead = skipMdeleteN(skipped.next, M, N)

    node.next = smallhead

    return nhead.next


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
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l)
