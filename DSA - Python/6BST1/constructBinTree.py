import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def printTreeInorder(node):
    if node is None:
        return
    
    printTreeInorder(node.left)
    print(node.data)
    printTreeInorder(node.right)


def createBinaryTreeLevelWise(arr):
    index = 0
    length = len(arr)
    if length<=0 or arr[0] == -1:
        return
    
    root = Node(arr[index])
    index+=1
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        currentNode = q.get()
        
        if arr[index] != -1:
            left = arr[index]
            index += 1
            leftNode = Node(left)
            currentNode.left = leftNode
            q.put(leftNode)
            
        
        if arr[index] != -1:
            right = arr[index]
            index += 1
            rightNode = Node(right)
            currentNode.right = rightNode
            q.put(rightNode)
    
    return root


inputElements = [int(i) for i in input().strip().split()]
root = createBinaryTreeLevelWise(inputElements)
printTreeInorder(root)