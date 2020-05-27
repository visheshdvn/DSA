class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    n = 1
    node = head
    nodes_list = []

    while n < i:
        if node == None:
            return head
        node = node.next
        n += 1

    a = Node(node.next.data)
    new_start = node.next.next
    n = i+2
    node.next = None

    nodes_list.append(head)
    nodes_list.append(a)


    new_node = new_start
    while n <= j:
        if new_node == None:
            return head
        new_node = new_node.next
        n += 1

    b = Node(new_node.data)

    new_third = new_node.next
    new_node.next = None

    nodes_list.append(new_start)
    nodes_list.append(b)
    nodes_list.append(new_third)

    node.next = nodes_list[3]
    node = node.next
    node.next = new_start
    new_node.next = nodes_list[1]
    new_node = new_node.next
    new_node.next = new_third

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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)
