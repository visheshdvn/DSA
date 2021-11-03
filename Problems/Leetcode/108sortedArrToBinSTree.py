import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if nums == []:
            return None
        
        n = len(nums)//2
        
        lchild = self.sortedArrayToBST(nums[:n])
        rchild = self.sortedArrayToBST(nums[n+1:])

        return TreeNode(nums[n], lchild, rchild)

def inOrder(root):

    if root == None:
        return

    inOrder(root.left)
    print(root.val, end=' ')
    inOrder(root.right)
    return


arr = [int(i) for i in input().strip().split()]
arr.sort()
ob = Solution()
root = ob.sortedArrayToBST(arr)
inOrder(root)
