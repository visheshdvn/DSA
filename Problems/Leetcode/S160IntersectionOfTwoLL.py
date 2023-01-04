class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

from typing import Optional

def getIntersectionNode(headA: Node, headB: Node) -> Optional[Node]:
    if headA is None or headB is None:
        return None

    node1 = headA
    node2 = headB
    
    while node1 != node2:
        if node1:
            node1 = node1.next
        else:
            node1 = headB
        
        if node2:
            node2 = node2.next
        else:
            node2 = headA
    
    return node1


def print_ll(head):
    node = head
    while node:
        print(node.data)
        node = node.next


def buildLL(nums):
    head = Node(nums[0])
    last = head

    for i in nums[1:]:
        last.next = Node(i)
        last = last.next

    return head


nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5]
headA = buildLL(nums1)
headB = buildLL(nums2)
headB.next = headA.next.next.next
node = getIntersectionNode(headA, headB)
print(node.data if node != None else None)