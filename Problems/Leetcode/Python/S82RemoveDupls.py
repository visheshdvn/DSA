class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_dupl(head):
    if head is None:
        return head

    pre_head = Node(-101)
    pre_head.next = head
    pre_itr = pre_head
    itr = head

    while itr and itr.next:
        if itr.data == itr.next.data:
            while itr.data == itr.next.data:
                itr = itr.next
                if itr.next == None:
                    break
            itr = itr.next
            continue
        else:
            pre_itr.next = itr
            itr = itr.next
            pre_itr = pre_itr.next

    pre_itr.next = itr
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


nums = [int(i) for i in input().strip().split()]
head = buildLL(nums)
new_head = remove_dupl(head)
print_ll(new_head)
