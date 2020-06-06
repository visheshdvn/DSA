import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, lst):
    if sum(lst) > k or root == None:
        return 0
    
    lst2 = lst[:]
    lst2.append(root.data)
    
    lch = rootToLeafPathsSumToK(root.left, k, lst2)
    rch = rootToLeafPathsSumToK(root.right, k, lst2)
    
    if lch == rch == 0 and sum(lst2) == k:
        print(*lst2)


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
rootToLeafPathsSumToK(root, k, [])
