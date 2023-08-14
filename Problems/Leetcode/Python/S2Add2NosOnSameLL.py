class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0

        c1 = l1
        c2 = l2
        while True:
            num = c1.val+c2.val+carry
            c1.val = num % 10
            carry = num // 10

            if not c1.next or not c2.next:
                if not c1.next and not c2.next and carry > 0:
                    node = ListNode(carry)
                    c1.next = node
                    return l1
                break

            c1 = c1.next
            c2 = c2.next
            

        if c1.next == None:
            c2 = c2.next
            c1.next = c2
            while c2:
                num = carry + c2.val
                c2.val = num % 10
                carry = num // 10
                if not c2.next:
                    break
                c2 = c2.next
            
            if carry != 0:
                node = ListNode(carry)
                c2.next = node

        elif c2.next == None:
            c1 = c1.next
            while c1:
                num = carry + c1.val
                c1.val = num % 10
                carry = num // 10
                if not c1.next:
                    break
                c1 = c1.next
            
            if carry != 0:
                node = ListNode(carry)
                c1.next = node
                
        return l1


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
