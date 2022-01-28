# Implement the BST class which includes following functions -
# 1. search
# Given an element, find if that is present in BSt or not. Return true or false.
# 2. insert -
# Given an element, insert that element in the BST at the correct position. Assume unique elements will be given.
# 3. delete -
# Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.
# 4. printTree (recursive) -
# Print the BST in ithe following format -
# For printing a node with data N, you need to follow the exact format -
# N:L:x,R:y
# wherer, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
# There is no space in between.
# You need to print all nodes in the recursive format in different lines.
# Note : main function is given for your reference which we are using internally to test the class.


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    
    def searchHelper(self, root, data):
        if root == None:
            return False
        
        if root.data == data:
            return True
        
        if root.data < data:
            val = self.searchHelper(root.right, data)
            
        if root.data > data:
            val = self.searchHelper(root.left, data)
        
        return False or val
    
    def search(self, data):
        return self.searchHelper(self.root, data)
        
    def insertHelper(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
        
        
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)
        
    def min(self, root):
        if root == None:
            return 10000
        
        if root.left == None:
            return root.data
        
        return self.min(root.left)
        
    def deleteHelper(self, root, data):
        if root == None:
            return False, None
        
        if root.data < data:
            deleted, newRightNode = self.deleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        
        if root.data > data:
            deleted, newLeftNode = self.deleteHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        
        if root.left == None and root.right == None:
            return True, None
        
        if root.left == None:
            return True, root.right
        
        if root.right == None:
            return True, root.left
        
        # 
        replacement = self.min(root.right)
        root.data = replacement
        deleted, newRightNode = self.deleteHelper(root.right, replacement)
        root.right = newRightNode
        return True, root
            
    def delete(self, data):
        deleted, newRoot = self.deleteHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted
    
    def count(self):
        return self.numNodes
    
    
b = BST()
li = [int(ele) for ele in input().split()]

i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1