# In a given Generic Tree, replace each node with its depth value. You need to just update the data of each node, no need to return or print anything.
# Input format :
# Line 1 : Elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1 : (Level wise, each level in new line)
# 0 
# 1 1 1 
# 2 2

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def replacewithDepth(tree, val):
    tree.data = val
    
    if len(tree.children) == 0:
        return
    
    for i in tree.children:
        replacewithDepth(i, val+1)

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

def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()  # Move to next Line

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
replacewithDepth(tree, 0)
printLevelAtNewLine(tree)
