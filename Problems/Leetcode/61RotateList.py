class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotate_n(head, n):
    if head is None or n == 0:
        return head

    count = 1
    node = head

    while node.next:
        count += 1
        node = node.next

    n_front = count-(n % count)

    if n_front == count:
        return head

    nnode = head

    i = 1
    while i < n_front:
        i += 1
        nnode = nnode.next

    new_head = nnode.next
    nnode.next = None

    node.next = head
    return new_head


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
new_head = rotate_n(head, n)
print_ll(new_head)
