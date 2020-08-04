class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)

def kruskal(edges, nVertices):
    parent = [i for i in range(nVertices)]
    edges.sort(key=lambda x: x.wt)
    count = 0
    
    output = []
    i = 0
    
    while count < (nVertices-1):
        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src, parent)
        destParent = getParent(currentEdge.dest, parent)
        
        if srcParent != destParent:
            output.append(currentEdge)
            count += 1
            parent[srcParent] = destParent
        i += 1
    return output


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
edges = []

for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src, dest, wt)
    edges.append(edge)

output = kruskal(edges, n)

for edge in output:
    if edge.src < edge.dest:
        print(str(edge.src) + " " + str(edge.dest) + " " + str(edge.wt))
    else:
        print(str(edge.dest) + " " + str(edge.src) + " " + str(edge.wt))
        