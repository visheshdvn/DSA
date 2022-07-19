# You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First and the only line of each test case or query contains the the elements of the singly linked list separated by a single space.

# Output format :
# For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.


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
