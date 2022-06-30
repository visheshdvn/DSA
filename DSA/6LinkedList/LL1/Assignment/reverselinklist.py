# You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
# To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.


#  Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.


# Output format :
# For each test case, print the singly linked list of integers in a reverse fashion, in a row, separated by a single space.

# Output for every test case will be printed in a seperate line.

# Sample Input 1 :
# 1
# 1 2 3 4 5 -1
# Sample Output 1 :
# 5 4 3 2 1


# Sample Input 2 :
# 2
# 1 2 3 -1
# 10 20 30 40 50 -1
# Sample Output 2 :
# 3 2 1
# 50 40 30 20 10

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linkedlist_spl(head):
    prev = head
    node = prev.next
    copy = None

    while node != None:
        prev.next = copy
        copy = prev
        prev = node
        node = node.next
    
    prev.next = copy

    while prev != None:
        print(prev.data, end= ' ')
        prev = prev.next

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
from sys import setrecursionlimit
setrecursionlimit(10000)
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
print_linkedlist_spl(l)
