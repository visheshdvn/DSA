import queue
from typing import Iterable


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirrorBinaryTree(root):
    q = queue.Queue()
    last_level = -1
    obj = {"node": root, "level": 0}
    q.put(obj)

    iterable = []
    while not q.empty():
        ob = q.get()
        if ob['level'] > last_level:
            # print(ob["node"].data)
            iterable.append(ob["node"].data)
            last_level += 1

        if ob["node"].left:
            q.put({"node": ob["node"].left, "level": ob['level'] + 1})

        if ob["node"].right:
            q.put({"node": ob["node"].right, "level": ob['level'] + 1})

    return iterable


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

# Problem ID 353, Level order traversal


def printLevelATNewLine(root):
    if root == None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
l = mirrorBinaryTree(root)

for i in l:
    print(i)
