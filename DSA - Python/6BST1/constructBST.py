import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(lst):
    if len(lst) == 0:
        return None

    if len(lst) == 1:
        return BinaryTreeNode(lst[0])

    mid = len(lst)//2 if n & 1 else len(lst)//2-1

    lnode = constructBST(lst[:mid])
    rnode = constructBST(lst[mid+1:])

    node = BinaryTreeNode(lst[mid])
    node.left = lnode
    node.right = rnode
    return node


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
lst = [int(i) for i in input().strip().split()]
root = constructBST(lst)
preOrder(root)


##
# 11 21 32 36 55 63 76 79 91 116 124 189 216 246 256 266 286 308 312 319 329 331 333 352 354 372 385 450 451 504 519 537 547 550 565 578 582 616 618 626 638 647 684 687 726 744 766 809 820 823 856 875 906 924 925 994
# 56 -> 27 | 28
# 55 -> 27 | 27
