import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p == q == None: return True

        if (p is None or q is None): return False

        if p.val != q.val: return False

        lresult = self.isSameTree(p.left, q.right)
        rresult = self.isSameTree(p.right, q.left)

        return lresult and rresult and p.val == q.val

    def isSymmetric(self, root):
        return self.isSameTree(root.left, root.right)


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


treedata = [int(i) for i in input().strip().split()]
root = buildLevelTree(treedata)
ob = Solution()
print(ob.isSymmetric(root))
