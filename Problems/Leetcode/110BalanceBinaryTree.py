import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalancedhelper(self, root):
        if not root:
            return 0, True

        lh, l_bool = self.isBalancedhelper(root.left)
        rh, r_bool = self.isBalancedhelper(root.right)

        return max(lh, rh) + 1, abs(lh-rh) < 2 and l_bool and r_bool

    def isBalanced(self, root):
        h, t = self.isBalancedhelper(root)
        print(h, t)
        return t


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


levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
ob = Solution()
print(ob.isBalanced(root))
