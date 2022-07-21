# Given a binary tree, print the tree in level wise order.
# For printing a node with data N, you need to follow the exact format -
# N:L:x,R:y
# wherer, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print -1. if any child is null.
# There is no space in between.
# You need to print all nodes in the level order form in different lines.
# Input format :
# Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Sample Input :
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output :
# 8:L:3,R:10
# 3:L:1,R:6
# 10:L:-1,R:14
# 1:L:-1,R:-1
# 6:L:4,R:7
# 14:L:13,R:-1
# 4:L:-1,R:-1
# 7:L:-1,R:-1
# 13:L:-1,R:-1

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    # Given a binary tree, print the tree in level wise order. For printing
    # a node with data N, you need to follow the exact format:
    # N:L:x,R:y
    # wherer, N is data of any node present in the binary tree. x and y are the
    # values of left and right child of node N. Print -1. if any child is null.
    # There is no space in between. You need to print all nodes in the level
    # order form in different lines.
    q = queue.Queue()

    q.put(root)

    while not q.empty():
        node = q.get()

        if node.left != None:
            q.put(node.left)
        else:
            node.left = BinaryTreeNode(-1)

        if node.right != None:
            q.put(node.right)
        else:
            node.right = BinaryTreeNode(-1)

        print(str(node.data) + ':L:' + str(node.left.data) +
              ',R:' + str(node.right.data))


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelWise(root)
