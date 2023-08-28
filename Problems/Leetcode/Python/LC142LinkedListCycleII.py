from typing import List, Optional


class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def detectCycle(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    is_crossed_at = {}
    node = head

    index = 0
    while node:
        ind = is_crossed_at.get(node, -1)

        if ind != -1:
            return node
        else:
            is_crossed_at[node] = index

        node = node.next
        index += 1

    return None


def createLL(arr: List[int]):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printLL(head: Node):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# arr = [int(i) for i in input().split()]
# head = createLL(arr)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2
res = detectCycle(None)
print(res)
