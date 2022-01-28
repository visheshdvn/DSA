# Given a generic tree, print the input tree in level wise order. ####For printing a node with data N, you need to follow the exact format -
# N:x1,x2,x3,...,xn
# wherer, N is data of any node present in the binary tree. x1, x2, x3, ...., xn are the children of node N
# There is no space in between.
# You need to print all nodes in the level order form in different lines.
# Input format :
# Elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Output Format :
# Level wise print
# Sample Input :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output :
# 10:20,30,40
# 20:40,50
# 30:
# 40:
# 40:
# 50:

import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(tree):
    q = queue.Queue()
    
    q.put(tree)
    
    while not q.empty():
        current_node = q.get()
        
        print(str(current_node.data)+":", end='')
        for i in range(len(current_node.children)):
            if i != len(current_node.children) - 1:
                print(current_node.children[i].data, end=',')
            else:
                print(current_node.children[i].data, end='')
                
            q.put(current_node.children[i])
            
        print('')


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
printLevelWiseTree(tree)
