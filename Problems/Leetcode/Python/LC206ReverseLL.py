class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_LL(head):
    if head is None or head.next is None:
        return head

    back = None
    mid = head
    front = head.next

    while mid:
        if front == None:
            mid.next = back
            break

        mid.next = back
        back = mid
        mid = front
        front = front.next

    return mid


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
new_head = reverse_LL(head)
print_ll(new_head)
