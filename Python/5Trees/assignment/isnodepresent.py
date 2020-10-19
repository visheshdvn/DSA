# Given a binary tree and an integer x, check if node with data x is present in the input binary tree or not. Return true or false.
# Input format :
# Line 1 : Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Line 2 : Integer x
# Output Format :
# true or false
# Sample Input :
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# 7
# Sample Output :
# true

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isNodePresent(root, x):
    if root == None:
        return False
    
    if root.data == x:
        return True
    
    return isNodePresent(root.left, x) or isNodePresent(root.right, x)

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
x=int(input())
present=isNodePresent(root, x)
if present:
    print('true')
else:
    print('false')
