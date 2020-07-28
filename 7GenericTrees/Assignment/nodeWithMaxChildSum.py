class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(tree):
    if tree == None:
        return 0
    
    if len(tree.children) == 0:
        return tree, 0
    
    sum = tree.data
    for i in tree.children:
        sum += i.data
    
    child_sum = 0
    for i in tree.children:
        c_node, child_sum = maxSumNode(i)
        
        if child_sum > sum:
            sum = child_sum
            tree = c_node
            
    return tree, sum    
    

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)
