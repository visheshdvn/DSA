import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def flatten(root):
    stack = queue.LifoQueue()
    stack2 = queue.LifoQueue()

    node = root
    while not stack.empty() or node is not None:
        while node is not None:
            # print(node.data)
            stack2.put(node)
            stack.put(node)
            node = node.left

        node = stack.get()
        node = node.right

    prev = None
    while not stack2.empty():
        node = stack2.get()
        node.left = None
        node.right = prev
        prev = node


def preOrderTraversal(root):
    stack = queue.LifoQueue()

    node = root
    while not stack.empty() or node is not None:
        while node is not None:
            print(node.data)
            stack.put(node)
            node = node.left

        node = stack.get()
        node = node.right


def printRightTree(root):
    node = root
    while node is not None:
        print(node.data)
        node = node.right


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
flatten(root)
printRightTree(root)
# preOrderTraversal(root)
