#!/usr/bin/env python
# coding: utf-8

# Given a a binary tree. Replace each of it's data with the depth of tree.
# Root is at depth 0, change its value to 0 and next level nodes are at depth 1 and so on.
# Print the tree after modifying in inorder fashion.
# Example:
# Input

# Alt text

# Output

# Alt text

# Input format :
# Line 1 :  Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Output Format :
#  Inorder traversal of modified tree.
# Sample Input 1:
#      1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Sample Output 1:
#      2 
#      1
#      2
#      0 
#      2 
#      1
#      2
# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def replaceWithDepth(root,level=0):
    if root == None:
        return
    
    root.data = level
    replaceWithDepth(root.left, level+1)
    replaceWithDepth(root.right, level+1)
    
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
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
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
replaceWithDepth(root)
inorder(root)

