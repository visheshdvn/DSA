#!/bin/python3
import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def mergeLists(head1, head2):
    new_head = SinglyLinkedListNode(-1)
    node = new_head

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            node.next = SinglyLinkedListNode(head1.data)
            node = node.next
            head1 = head1.next
        elif head2.data < head1.data:
            node.next = SinglyLinkedListNode(head2.data)
            node = node.next
            head2 = head2.data
        else:
            node.next = SinglyLinkedListNode(head1.data)
            node.next.next = SinglyLinkedListNode(head2.data)
            node = node.next.next
            head1 = head1.next
            head2 = head2.next

    while head1 is not None:
        node.next = SinglyLinkedListNode(head1.data)
        head1 = head1.next
        node = node.next

    while head2 is not None:
        node.next = SinglyLinkedListNode(head2.data)
        head2 = head2.next
        node = node.next

    return new_head.next


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        while llist3:
            print(llist3.data, end=" ")
            llist3 = llist3.next
