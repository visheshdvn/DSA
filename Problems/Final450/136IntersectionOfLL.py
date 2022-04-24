class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def intersection(L1, L2):
    if not L1 or not L2:
        return None

    pre_head = Node(0)
    node = pre_head

    while L1 and L2:
        if L1.data < L2.data:
            L1 = L1.next
        elif L2.data < L1.data:
            L2 = L2.next
        else:
            node.next = Node(L1.data)
            L1 = L1.next
            L2 = L2.next
            node = node.next

    return pre_head.next


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


nums1 = [int(i) for i in input().strip().split()]
nums2 = [int(i) for i in input().strip().split()]

head1 = buildLL(nums1)
head2 = buildLL(nums2)
new_head = intersection(head1, head2)
print_ll(new_head)
