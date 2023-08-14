class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def partition(head, x):
    if head is None or head.next is None:
        return head

    node = Node(0)
    node.next = head

    back = node
    front = node
    temp = None

    while front.next is not None:
        if front.next.data < x:
            temp = front.next
            front.next = front.next.next

            temp.next = back.next
            back.next = temp
            back = back.next
            if back == front.next:
                front = front.next
            continue

        front = front.next

    return node.next


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


x = int(input())
nums = [int(i) for i in input().strip().split()]
head = buildLL(nums)
new_head = partition(head, x)
print_ll(new_head)
