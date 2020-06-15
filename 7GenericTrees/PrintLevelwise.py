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
