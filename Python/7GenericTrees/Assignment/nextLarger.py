# Given a generic tree and an integer n. Find and return the node with next larger element in the Tree i.e. find a node with value just greater than n.
# Return NULL if no node is present with the value greater than n.
# Input Format :
# Line 1 : Integer n
# Line 2 : Elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Output Format :
# Node with value just greater than n.
# Sample Input 1 :
# 18
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1 :
# 20
# Sample Input 2 :
# 21
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 2:
# 30


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def nextLargest(tree, n):
    
    if len(tree.children) == 0:
        return tree
    
    ret_node = tree
    for i in tree.children:
        node = nextLargest(i, n)
        
        if (node.data > n and node.data < ret_node.data) or ret_node.data <= n:
            ret_node = node
            

    return ret_node


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
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
node = nextLargest(tree, n)
if node.data > n:
    print(node.data)
