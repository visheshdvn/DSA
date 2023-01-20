from typing import Optional


class ListNode:
    def __init__(self, data: int) -> None:
        self.data: str = data
        self.next: ListNode = None


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    back: ListNode = None
    node: ListNode = head

    while left > 1:
        back = node
        node = node.next
        left -= 1
        right -= 1

    connection: ListNode = back
    tail: ListNode = node

    while right > 0:
        front: ListNode = node.next
        node.next = back
        back = node
        node = front

        right -= 1

    if connection is not None:
        connection.next = back
    else:
        head = back

    tail.next = node
    return head


def buildLL(nums) -> ListNode:
    if len(nums) == 0:
        return None

    head = ListNode(nums[0])
    last = head

    for i in nums[1:]:
        last.next = ListNode(i)
        last = last.next

    return head


def printLL(node: ListNode):
    node = head
    while node:
        print(node.data)
        node = node.next


nums = [int(i) for i in input().strip().split()]

head = buildLL(nums)
nhead = reverseBetween(head, int(input()), int(input()))
printLL(nhead)
