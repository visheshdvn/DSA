class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_LL(head):
    if head is None or head.next is None:
        return head

    if not head or not head.next:
        return True

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        

def buildLL(nums):
    head = Node(nums[0])
    last = head

    for i in nums[1:]:
        last.next = Node(i)
        last = last.next

    return head


def print_ll(head):
    node = head
    while node:
        print(node.data)
        node = node.next


nums = [int(i) for i in input().strip().split()]
head = buildLL(nums)
new_head = reverse_LL(head)
print_ll(new_head)
