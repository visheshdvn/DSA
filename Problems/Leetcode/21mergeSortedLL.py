# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        newHead = ListNode(0)
        retHead = newHead

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                newHead.next = ListNode(l1.val)
                l1 = l1.next
                newHead = newHead.next
            elif l1.val > l2.val:
                newHead.next = ListNode(l2.val)
                l2 = l2.next
                newHead = newHead.next
            else:
                newHead.next = ListNode(l1.val)
                newHead.next.next = ListNode(l2.val)
                newHead = newHead.next.next
                l1 = l1.next
                l2 = l2.next

        while l1 != None:
            newHead.next = ListNode(l1.val)
            l1 = l1.next
            newHead = newHead.next

        while l2 != None:
            newHead.next = ListNode(l2.val)
            l2 = l2.next
            newHead = newHead.next

        return retHead.next


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
arr2 = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1)
l2 = ll(arr2)

ob = Solution()

l = ob.mergeTwoLists(l1, l2)
printll(l)
