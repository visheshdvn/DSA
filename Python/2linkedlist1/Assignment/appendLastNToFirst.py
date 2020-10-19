# You have been given a singly linked list of integers along with an integer 'N'. Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space. 

# The second line contains the integer value 'N'. It denotes the number of nodes to be moved from last to the front of the singly linked list.

# Output format :
# For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.

# Output for every test case will be printed in a seperate line.


# Sample Input 1 :
# 2
# 1 2 3 4 5 -1
# 3
# 10 20 30 40 50 60 -1
# 5
# Sample Output 1 :
# 3 4 5 1 2
# 20 30 40 50 60 10
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n, lth):
    t = lth
    node = head
    while t:
        node = node.next
        t-=1

    node.next = head

    t = lth - (n % (lth+1))
    while t:
        head = head.next
        t-=1
    
    new_head = head.next
    head.next = None
    return new_head

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
l = append_LinkedList(l, i, len(arr) - 2)
printll(l)
