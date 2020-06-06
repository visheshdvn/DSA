#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 1567, Find the minimum and maximum value
def minMax(root):
    
    if root == None:
        return None, None
    
    max_left, min_left = minMax(root.left)
    max_right, min_right = minMax(root.right)
    
    items = [max_left, min_left, max_right, min_right]
    
    to_return = [root.data]
    for i in items:
        if i != None:
            to_return.append(i)
            
    return max(to_return), min(to_return)
    
    

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
maximum, minimum = minMax(root)
print(maximum, minimum)

