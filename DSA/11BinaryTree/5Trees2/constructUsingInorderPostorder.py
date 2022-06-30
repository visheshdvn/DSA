# Given Postorder and Inorder traversal of a binary tree, create the binary tree associated with the traversals.You just need to construct the tree and return the root.
# Note: Assume binary tree contains only unique elements.
# Input format :

# Line 1 : n (Total number of nodes in binary tree)

# Line 2 : Post order traversal

# Line 3 : Inorder Traversal

# Output Format :

# Elements are printed level wise, each level in new line (separated by space).

# Sample Input :
# 8
# 8 4 5 2 6 7 3 1
# 4 8 2 5 1 6 3 7
# Sample Output :
# 1 
# 2 3 
# 4 5 6 7 
# 8

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    # Given Postorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 8 Nodes with following input:
    # postOrder: 8 4 5 2 6 7 3 1
    # inOrder: 4 8 2 5 1 6 3 7
    if inorder == []:
        return None
    
    root = BinaryTreeNode(postOrder.pop())
    
    rightNode = buildTreePostOrder(postOrder, inorder[inorder.index(root.data)+1: ])
    leftNode = buildTreePostOrder(postOrder, inorder[: inorder.index(root.data)])
    
    
    root.right = rightNode
    root.left = leftNode
        
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
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
