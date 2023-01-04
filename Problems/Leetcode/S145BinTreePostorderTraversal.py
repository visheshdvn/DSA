# Given a binary tree, print the postorder traversal of given tree.
# Post-order traversal is: LeftChild RightChild Root
# Input format :
# Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Output Format :
# Post-order traversal, elements separated by space
# Sample Input :
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output :
# 1 4 7 6 3 13 14 10 8

import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrder(root):
    # Given a binary tree, print the postorder traversal of given tree.
    # Post-order traversal is: LeftChild RightChild Root

    if root == None:
        return []

    llst = postOrder(root.left)
    rlst = postOrder(root.right)

    return [*llst, *rlst, root.data]


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
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
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

list = postOrder(root)

for i in list:
    print(i)
