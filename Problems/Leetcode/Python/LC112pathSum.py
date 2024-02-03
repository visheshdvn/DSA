import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSumHelper(self, root, targetsum, curr=0):
        if root == None:
            return False

        if root.left == None and root.right == None and curr+root.val == targetsum:
            return True

        rbool = self.hasPathSumHelper(root.right, targetsum, curr+root.val)
        lbool = self.hasPathSumHelper(root.left, targetsum, curr+root.val)

        return rbool or lbool

    def hasPathSum(self, root, targetSum):
        return self.hasPathSumHelper(root, targetSum)


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


targetSum = int(input())
arr = [int(i) for i in input().strip().split()]
root = buildLevelTree(arr)
ob = Solution()
print(ob.hasPathSum(root, targetSum))
