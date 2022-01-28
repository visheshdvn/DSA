# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        if head is None:
            return head

        prev_head = ListNode(-1)
        prev_head.next = head

        node = head
        prev = prev_head

        while node:
            if node.val == val:
                node = node.next
            else:
                prev.next = node
                prev = prev.next
                node = node.next

        prev.next = node
        return prev_head.next


def ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    last = head
    for data in arr[1:]:
        last.next = ListNode(data)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


arr1 = list(int(i) for i in input().strip().split(' '))
n = int(input())

# Create a Linked list after removing -1 from list
head = ll(arr1)

ob = Solution()
l = ob.removeElements(head, n)
printll(l)
