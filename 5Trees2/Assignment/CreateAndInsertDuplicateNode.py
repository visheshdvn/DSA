# Not Working

# Given a Binary Tree with N number of nodes, for each node create a new duplicate node, and insert that duplicate as left child of the original node.
# Note : Root will remain same. So you just need to insert nodes in the given Binary Tree and no need to print or return anything.
# Input format :
# Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Output Format :
# Level order traversal of updated tree. (Every level in new line)
# Constraints :
# 1 <= N <= 1000
# Sample Input :
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# Sample Output :
# 8 
# 8 10 
# 5 10 
# 5 6 
# 2 6 7 
# 2 7

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertDuplicateNode(root):
    if root == None:
        return
    
    insertDuplicateNode(root.left)
    
    node = BinaryTreeNode(root.data)
    node.right = root.right
    node.left = root.left
    root.left = node
    
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

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
insertDuplicateNode(root)
printLevelATNewLine(root)
