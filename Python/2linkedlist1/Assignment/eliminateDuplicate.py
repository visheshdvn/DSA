# You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.

#  Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first and the only line of each test case or query contains the elements(in ascending order) of the singly linked list separated by a single space.

#  Output format :
# For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.

# Output for every test case will be printed in a seperate line.

# Sample Input 1 :
# 1
# 1 2 3 3 4 3 4 5 4 5 5 7 -1
# Sample Output 1 :
# 1 2 3 4 3 4 5 4 5 7 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    # new_head = head
    prev = head
    node = prev.next

    while node != None:
        if prev.data != node.data:
            prev.next = node
            prev = prev.next

        if prev.data == node.data:
            prev.next = node.next
            node = node.next

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
l = eliminate_duplicate(l)
printll(l)
