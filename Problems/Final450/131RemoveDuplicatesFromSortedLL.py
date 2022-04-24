class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_dupl(head):
    if head is None:
        return head
    
    prev = head
    ahead = head.next
    
    while ahead:
        if prev.data == ahead.data:
            ahead = ahead.next
        else:
            prev.next = ahead
            ahead = ahead.next
            prev = prev.next
		
    prev.next = ahead
    return head


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
new_head = remove_dupl(head)
print_ll(new_head)