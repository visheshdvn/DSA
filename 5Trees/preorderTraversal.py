# Given a binary tree, print the preorder traversal of given tree.
# Pre-order traversal is: Root LeftChild RightChild
# Input format :
# Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Output Format :
# Pre-order traversal, elements separated by space
# Sample Input :
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output :
# 8 3 1 6 4 7 10 14 13

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    
    if root == None:
        return
    
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)
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
preOrder(root)
