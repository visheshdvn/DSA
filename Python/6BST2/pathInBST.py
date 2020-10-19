# Given a BST and an integer k. Find and return the path from the node with data k and root (if a node with data k is present in given BST). Return null otherwise.
# Assume that BST contains all unique elements.
# Input Format :
# Line 1 : Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Line 2 : Integer k
# Output Format :
# Path from node k to root
# Sample Input :
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 2
# Sample Output :
# 2
# 5
# 8


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPathBST(root,data):
    if root == None:
        return
    
    if root.data == data:
        print(root.data)
        return True
    
    if root.data < data:
        val = findPathBST(root.right, data)
        
    if root.data > data:
        val = findPathBST(root.left, data)
    
    if val:
        print(root.data)
        return val
    
    return 


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
data = int(input())
findPathBST(root,data)