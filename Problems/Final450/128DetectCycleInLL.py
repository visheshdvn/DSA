from types import new_class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head

    while fast.next and slow.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

        if not slow or not fast:
            return False

    return False


def buildLL(nums):
    head = Node(nums[0])
    last = head

    for i in nums[1:]:
        last.next = Node(i)
        last = last.next

    return head


nums = [int(i) for i in input().strip().split()]
head = buildLL(nums)
print(detect_cycle(head))
