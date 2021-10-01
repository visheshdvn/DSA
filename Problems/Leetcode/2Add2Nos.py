class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0

        sum_node = ListNode(0)
        trav = sum_node
        while l1 and l2:
            num = carry + l1.val + l2.val
            ones = num % 10
            carry = num // 10

            node = ListNode(ones)
            trav.next = node
            trav = trav.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            num = carry + l1.val
            ones = num % 10
            carry = num//10
            
            node = ListNode(ones)
            trav.next = node
            trav = trav.next
            
            l1 = l1.next
        
        while l2:
            num = carry + l2.val
            ones = num % 10
            carry = num//10
            
            node = ListNode(ones)
            trav.next = node
            trav = trav.next
            
            l2 = l2.next

        if carry == 0:
            return sum_node.next
        
        nnode = ListNode(carry)
        trav.next = nnode
        trav = trav.next    
        return sum_node.next


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

head1 = ll(arr1)
head2 = ll(arr2)
ob = Solution()
printll(ob.addTwoNumbers(head1, head2))
