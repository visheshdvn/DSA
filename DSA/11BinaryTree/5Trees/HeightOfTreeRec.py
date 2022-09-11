#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# Given a binary tree, find and return the height of given tree.
# Input format :
# Nodes in the level order form (separated by space). If any node does not have left or right child, take -1 in its place
# Output format :
# Height
# Constraints :
# 1 <= N <= 10^5
# Sample Input :
# 10
#  9
# 4
# -1
# -1
#  5
#  8
# -1
# 6
# -1
# -1
# 3
# -1
# -1
# -1
# Sample Output :
# 5

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root == None:
        return 0

    l = height(root.left)
    r = height(root.right)
    
    return max(l, r) + 1


def buildLevelTree():

    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
root = buildLevelTree()
print(height(root))
