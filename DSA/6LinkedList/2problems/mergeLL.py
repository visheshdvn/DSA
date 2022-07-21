# Given two linked lists sorted in increasing order. Merge them in such a way that the result list is also sorted (in increasing order).
# Try solving with O(1) auxiliary space (in-place). You just need to return the head of new linked list, don't print the elements.
# Input format :
# Line 1 : Linked list 1 elements of length n (separated by space and terminated by -1)
# Line 2 : Linked list 2 elements of length m (separated by space and terminated by -1)
# Output format :
# Merged list elements (separated by space)
# Constraints :
# 1 <= n, m <= 10^4
# Sample Input :
#  2 5 8 12 -1
#  3 6 9 -1
# Sample Output :
#  2 3 5 6 8 9 12

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNodeandReturn(a):
    node = Node(a)
    return node


def merge(head1, head2):
    newHead = Node(0)
    retHead = newHead

    while head1 != None and head2 != None:
        if head1.data < head2.data:
            newHead.next = createNodeandReturn(head1.data)
            head1 = head1.next
            newHead = newHead.next
        elif head1.data > head2.data:
            newHead.next = createNodeandReturn(head2.data)
            head2 = head2.next
            newHead = newHead.next
        else:
            newHead.next = createNodeandReturn(head1.data)
            newHead.next.next = createNodeandReturn(head2.data)
            newHead = newHead.next.next
            head1 = head1.next
            head2 = head2.next

    while head1 != None:
        newHead.next = createNodeandReturn(head1.data)
        head1 = head1.next
        newHead = newHead.next

    while head2 != None:
        newHead.next = createNodeandReturn(head2.data)
        head2 = head2.next
        newHead = newHead.next

    return retHead.next


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
arr1 = list(int(i) for i in input().strip().split(' '))
arr2 = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)
