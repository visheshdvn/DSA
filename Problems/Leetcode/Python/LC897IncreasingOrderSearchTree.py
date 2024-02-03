import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Basic Solution
class Solution:
#     def queueBuilder(self, root):
#         if root == None:
#             return None

#         self.queueBuilder(root.left)
#         self.queue.put(root)
#         self.queueBuilder(root.right)

#     def increasingBST(self, root):
#         if not root.left and not root.right:
#             return root

#         self.queue = queue.Queue()
#         self.queueBuilder(root)

#         new_root = self.queue.get()
#         new_root.left = None
#         new_root.right = None
#         new_root_itr = new_root

#         while not self.queue.empty():
#             node = self.queue.get()
#             node.left = None
#             node.right = None

#             new_root_itr.right = node
#             new_root_itr = new_root_itr.right

#         return new_root

# Optimized Solution
    def queueBuilder(self, root):
        if root == None:
            return None

        self.queueBuilder(root.left)
        self.newRootPointer.right = BinaryTreeNode(root.data)
        self.newRootPointer = self.newRootPointer.right
        self.queueBuilder(root.right)

    def increasingBST(self, root):
        if not root.left and not root.right:
            return root

        self.newRoot = BinaryTreeNode(0)
        self.newRootPointer = self.newRoot
        self.queueBuilder(root)
        root = None
        return self.newRoot.right

### Best Solution
    # def increasingBST(self, root):
        # dummy = BinaryTreeNode()
        # temp = dummy
        # stack = []
        # while stack or root:  #I have given two condition bcz fist time my stack is empty
        #     while root:
        #         stack.append(root)  #In inorder traversal we fist go on left side until we got null 
        #         root = root.left
        #     endRoot = stack.pop()   #pop last value
        #     temp.right = BinaryTreeNode(endRoot.data)   #creating Node on rightside of temp
        #     temp = temp.right   # updating temp  this process is similar like adding element in linkedlist

            
        #     root = endRoot.right  # after visiting all nodes in left we go in right direction in Inorder traversal 

        # return dummy.right  # return dummy.right because our dummy start with initialization which is 0


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


def printLevelATNewLine(root):
    if root == None:
        return
    node = root

    while node:
        print(node.data)
        node = node.right


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
ob = Solution()
new_head = ob.increasingBST(root)
printLevelATNewLine(new_head)
