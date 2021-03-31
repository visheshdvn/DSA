# Given a sorted integer array A of size n which contains all unique elements. You need to construct a balanced BST from this input array. Return the root of constructed BST.
# Note : If array size is even, take first mid as root.
# Input format :
# Line 1 : Integer n (Size of array)
# Line 2 : Array elements (separated by space)
# Output Format :
# BST elements (in pre order traversal, separated by space)
# Sample Input :
# 7
# 1 2 3 4 5 6 7
# Sample Output :
# 4 2 1 3 6 5 7


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    if lst == []:
        return None
    
    n = len(lst)
    if n&1:
        mid_ind = n//2
    else:
        mid_ind = n//2 - 1
    node = BinaryTreeNode(lst[mid_ind])
    
    l_node = constructBST(lst[: mid_ind])
    r_node = constructBST(lst[mid_ind+1 :])
    
    node.left = l_node
    node.right = r_node
    
    return node


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)


##
# 11 21 32 36 55 63 76 79 91 116 124 189 216 246 256 266 286 308 312 319 329 331 333 352 354 372 385 450 451 504 519 537 547 550 565 578 582 616 618 626 638 647 684 687 726 744 766 809 820 823 856 875 906 924 925 994
# 56 -> 27 | 28
# 55 -> 27 | 27