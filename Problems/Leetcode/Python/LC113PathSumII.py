import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreeInorder(node):
    if node is None:
        return
    
    printTreeInorder(node.left)
    print(node.val)
    printTreeInorder(node.right)

class Solution:
    def hasPathSumHelper(self, root, targetSum, carr=[], csum=0):
        if (root == None and csum != targetSum) or (csum > targetSum):
            return []
        
        if (root == None and csum == targetSum):
            return [] if csum == 0  else [carr]
        
        if root.left == None and root.right == None and csum + root.val == targetSum:
            return [[*carr, root.val]]
        
        l_arr = self.hasPathSumHelper(root.left, targetSum, [*carr, root.val], csum+root.val)
        r_arr = self.hasPathSumHelper(root.right, targetSum, [*carr, root.val], csum+root.val)
        
        return [*l_arr, *r_arr]

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
# printTreeInorder(root)
