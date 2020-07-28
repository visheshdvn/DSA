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
