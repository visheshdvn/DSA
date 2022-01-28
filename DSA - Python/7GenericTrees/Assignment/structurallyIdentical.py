# Given two Generic trees, return true if they are structurally identical i.e. they are made of nodes with the same values arranged in the same way.
# Input format :
# Line 1 : Tree 1 elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Line 2 : Tree 2 elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Output format :
# true or false
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output 1 :
# true
# Sample Input 2 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 10 3 2 30 40 2 40 50 0 0 0 0
# Sample Output 2:
# false


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def testTrees(tree):
    lst = []
    
    n = len(tree.children)
    if n == 0:
        return [tree.data, 0]
    
    for i in tree.children:
        clst = testTrees(i)
        lst += clst
        
    lst += [tree.data, n]
    return lst 


def isIdentical(tree1, tree2):
    res1 = testTrees(tree1)
    res2 = testTrees(tree2)
    return res1 == res2

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
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')
