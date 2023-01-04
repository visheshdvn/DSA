class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_nth(head, n):
    if head is None:
        return head

    count = 0

    node = head
    while node:
        count += 1
        node = node.next

    n_front = count+1-n

    temp_node = Node(-1)
    temp_node.next = head
    nnode = temp_node

    i = 0
    while i < n_front-1:
        i += 1
        nnode = nnode.next

    nnode.next = nnode.next.next

    return temp_node.next


def buildLL(nums):
    head = Node(nums[0])
    last = head

    for i in nums[1:]:
        last.next = Node(i)
        last = last.next

    return head


def print_ll(head):
    node = head
    while node:
        print(node.data)
        node = node.next


nums = [int(i) for i in input().strip().split()]
n = int(input())
head = buildLL(nums)
new_head = remove_nth(head, n)
print_ll(new_head)
