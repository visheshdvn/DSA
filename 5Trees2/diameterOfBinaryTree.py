# Given a Binary Tree, find and return the diameter of input binary tree.
# Diameter is - largest count of nodes between any two leaf nodes in the binary tree (both the leaf nodes are inclusive).
# Input format :
# Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Output Format :
# diameter
# Sample Input :
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output :
# 7

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def height(root):
    if root == None:
        return 0
    
    return 1 + max(height(root.left), height(root.right))
    
def diameter(root):
    if root == None:
        return 0
    
    left_h = height(root.left)
    right_h = height(root.right)
    
    left_diamtr = diameter(root.left)
    right_diamtr = diameter(root.right)
    
    return max(left_h + right_h + 1, max(left_diamtr, right_diamtr))

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
print(diameter(root))
