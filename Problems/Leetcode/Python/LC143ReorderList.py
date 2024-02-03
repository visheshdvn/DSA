from queue import LifoQueue, Queue
from typing import Optional


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def reorderList(head: Optional[ListNode]) -> None:
    if head is None or head.next is None:
        return head

    q = Queue()
    s = LifoQueue()

    slow: ListNode = head
    fast: ListNode = head.next
    q.put(slow)

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        q.put(slow)

    while slow:
        slow = slow.next
        if slow:
            s.put(slow)

    # creting the new ll
    n_head: ListNode = ListNode(-1)
    # n_node: ListNode = n_head
    while not q.empty() and not s.empty():
        n_head.next = q.get()
        n_head.next.next = s.get()
        n_head = n_head.next.next

    if not q.empty():
        n_head.next = q.get()
        n_head = n_head.next

    n_head.next = None


def reorderList2(head: Optional[ListNode]) -> None:
    if head is None or head.next is None:
        return head

    slow: ListNode = head
    fast: ListNode = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev = slow.next = None  
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp 

    # rearranging
    first, second = head, prev
    
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2 


def print_ll(head: ListNode):
    node = head
    while node:
        print(node.data)
        node = node.next


def buildLL(nums):
    head = ListNode(nums[0])
    last: ListNode = head

    for i in nums[1:]:
        last.next = ListNode(i)
        last = last.next

    return head


nums1 = [int(i) for i in input().strip().split()]
head = buildLL(nums1)
reorderList2(head)
print_ll(head)
