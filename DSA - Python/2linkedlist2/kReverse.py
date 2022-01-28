# Implement kReverse( int k ) in a linked list i.e. you need to reverse first K elements then reverse next k elements and join the linked list and so on.
# Indexing starts from 0. If less than k elements left in the last, you need to reverse them as well. If k is greater than length of LL, reverse the complete LL.
# You don't need to print the elements, just return the head of updated LL.

# Input format :
# Line 1 : Linked list elements (separated by space and terminated by -1)
# Line 2 : k

# Sample Input 1 :
# 1 2 3 4 5 6 7 8 9 10 -1
# 4
# Sample Output 1 :
# 4 3 2 1 8 7 6 5 10 9
# Sample Input 2 :
# 1 2 3 4 5 -1
# 2
# Sample Output 2 :
# 2 1 4 3 5 
# Sample Input 3 :
# 1 2 3 4 5 6 7 -1
# 3
# Sample Output 3 :
# 3 2 1 6 5 4 7

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
