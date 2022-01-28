# Given a BST and an integer k. Find if the integer k is present in given BST or not. Return the node with data k if it is present, return null otherwise.
# Assume that BST contains all unique elements.
# Input Format :
# Line 1 : Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Line 2 : Integer k
# Output Format :
# Node with data k
# Sample Input 1 :
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 2
# Sample Output 1 :
# 2
# Sample Input 2 :
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 12
# Sample Output 2 :
# (empty)

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def searchInBST(root, k):
    if root == None:
        return None
    
    if root.data == k:
        return root
    
    if k < root.data:
        res = searchInBST(root.left, k)
    else:
        res = searchInBST(root.right, k)
        
    return None or res


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
k=int(input())
node=searchInBST(root, k)
if node:
    print(node.data)
