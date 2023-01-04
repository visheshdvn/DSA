# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        
        prev = head
        ahead = head.next

        while ahead:
            if prev.val == ahead.val:
                ahead = ahead.next
            else:
                prev.next = ahead
                ahead = ahead.next
                prev = prev.next

        prev.next = ahead

        return head


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
# Create a Linked list after removing -1 from list
head = ll(arr1)

ob = Solution()

l = ob.deleteDuplicates(head)
printll(l)
