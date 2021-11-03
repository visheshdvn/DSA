import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1

        ld = float("inf")
        rd = float("inf")

        if root.left:
            ld = self.minDepth(root.left)

        if root.right:
            rd = self.minDepth(root.right)

        return 1+min(ld, rd)


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = TreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = TreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = TreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


arr = [int(i) for i in input().strip().split()]
root = buildLevelTree(arr)
ob = Solution()
print(ob.minDepth(root))
