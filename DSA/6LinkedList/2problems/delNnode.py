class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteHelper(head, N):
    t = head
    while N:
        if t.next == None:
            return None
        t = t.next
        N-=1
    return t

def skipMdeleteN(head, M, N):
    if M == N == 0:
        return None

    if N == 0:
        return head

    if M == 0 and N != 0:
        return None

    nhead = Node(0)
    nhead.next = head
    
    val = 0
    while nhead.next:
        val+=1
        nhead = nhead.next
        if nhead == None:
            break
        if val != M:
            continue
        
        node = deleteHelper(nhead, N+1)
        nhead.next = node
        val = 0
    
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
l = ll(arr[:-1])
m = int(input())
n = int(input())
l = skipMdeleteN(l, m, n)
printll(l)
