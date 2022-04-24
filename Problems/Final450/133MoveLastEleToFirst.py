class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def move_item(head):
    if not head.next:
        return head

    node = head

    while node.next.next is not None:
        node = node.next

    new_head = node.next
    node.next = None
    new_head.next = head

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
head = buildLL(nums)
new_head = move_item(head)
print_ll(new_head)
