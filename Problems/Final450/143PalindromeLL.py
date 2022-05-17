class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_palindrome(head):
    stack = []
    if not head or not head.next:
        return True

    slow = head
    fast = head.next
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:
        stack.append(slow.data)    
    slow = slow.next

    while slow:
        if stack[-1] == slow.data:
            stack.pop()
            slow = slow.next
        else:
            return False

    return len(stack) == 0


def buildLL(nums):
    head = Node(nums[0])
    last = head

    for i in nums[1:]:
        last.next = Node(i)
        last = last.next

    return head


nums = [int(i) for i in input().strip().split()]
head = buildLL(nums)
print(is_palindrome(head))
