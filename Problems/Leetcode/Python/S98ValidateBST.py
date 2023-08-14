import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        if root is None:
            return True, []

        # if (root.left and root.val <= root.left.val) or (root.right and root.val >= root.right.val):
        #     return False

        lbool, lres = self.isValidBST(root.left)
        rbool, rres = self.isValidBST(root.right)

        if lbool is False or rbool is False:
            return False, []

        if lres == rres == []:
            return True, [root.val]

        pass


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
print(ob.isValidBST(root))
