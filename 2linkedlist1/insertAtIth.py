class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def insertIth(head, n, data):
    if n < 1:
        return head

    if n == 1:
        newNode = Node(data)
        newNode.next = head
        head = newNode
        return head

    curr = head
    ahd = head.next

    while n > 2:
        curr = curr.next
        ahd = ahd.next
        n -=1

        if ahd.next is None and n > 2:
            return head
    
    newNode = Node(data)
    newNode.next = ahd
    curr.next = newNode
    
    return head
    


def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


arr = [int(i) for i in input().strip().split(' ')]
n = int(input())
data = int(input())
head = ll(arr)

head = insertIth(head, n, data)
printLL(head)
