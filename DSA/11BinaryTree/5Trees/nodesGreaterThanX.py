
# Given a Binary Tree and an integer x, find and return the count of nodes which are having data greater than x.
# Input format :
# Line 1 : Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Line 2 : Integer x
# Output Format :
# count
# Sample Input :
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# 8
# Sample Output :
# 3

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countNodesGreaterThanX(root, x):
    if root == None:
        return 0

    nleft = countNodesGreaterThanX(root.left, x)
    nright = countNodesGreaterThanX(root.right, x)

    if root.data > x:
        return 1+nleft+nright
    else:
        return nleft+nright


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
x = int(input())
root = buildLevelTree(levelOrder)
print(countNodesGreaterThanX(root, x))
