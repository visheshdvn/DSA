# Given a binary tree, a node and an integer K, print nodes which are at K distance from the the given node.
# Input format :

# Line 1 : Elements in level order form (separated by space)

# (If any node does not have left or right child, take -1 in its place)

# Line 2 : Node

# Line 3 : K

# Output format : Answer nodes in different line

# Sample Input :
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# 3
# 1
# Sample Output :
# 9
# 6

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def searchNodeAtDist(root, dist):
    if root == None:
        return 0
    
    if dist == 0:
        print(root.data)
        
    searchNodeAtDist(root.left, dist-1)
    searchNodeAtDist(root.right, dist-1)
    
    return
    

def printNodeAtDistanceKFromNode(root, node, distance):
    if root == None:
        return -1
    
    if root.data == node:
        searchNodeAtDist(root, distance)
        return 1
    
    left_dist = printNodeAtDistanceKFromNode(root.left, node, distance)
    if left_dist > 0:
        if left_dist == distance:
            searchNodeAtDist(root, 0)
            exit(0)
        searchNodeAtDist(root.right, distance - left_dist -1)
        return 1 + left_dist
    
    right_dist = printNodeAtDistanceKFromNode(root.right, node, distance)
    if right_dist > 0:
        if right_dist == distance:
            searchNodeAtDist(root, 0)
            exit(0)
        searchNodeAtDist(root.left, distance - right_dist -1)
        return 1 + right_dist
    
    return -1

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
node=int(input())
distance=int(input())
printNodeAtDistanceKFromNode(root, node, distance)
