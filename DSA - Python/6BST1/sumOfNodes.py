import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumOfAllNodes(root):
    if root is None:
        return 0
    
    a = root.data
    leftval = sumOfAllNodes(root.left)
    rightval = sumOfAllNodes(root.right)
    return a + leftval + rightval
    

def buildLevelTree(arr):
    index = 0
    length = len(arr)
    if length<=0 or arr[0] == -1:
        return
    
    root = BinaryTreeNode(arr[index])
    index+=1
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        currentNode = q.get()
        
        if arr[index] != -1:
            left = arr[index]
            index += 1
            leftNode = BinaryTreeNode(left)
            currentNode.left = leftNode
            q.put(leftNode)
            
        
        if arr[index] != -1:
            right = arr[index]
            index += 1
            rightNode = BinaryTreeNode(right)
            currentNode.right = rightNode
            q.put(rightNode)
    
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
sum = sumOfAllNodes(root)
print(sum)
# print(sumOfAllNodes(root))
