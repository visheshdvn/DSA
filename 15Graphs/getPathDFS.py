class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def dfsHelper(self, sv, v2, visited):
        visited[sv] = True
        if sv == v2:
            return [v2]
        
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                val = self.dfsHelper(i, v2, visited)
                if val is not None:
                    val.append(sv)
                    return val
            
        return None
        
    
    def dfsPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        lst = self.dfsHelper(v1, v2, visited)
        return lst
        
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __str__(self):
        return str(self.adjMatrix)


V, E = [int(i) for i in input().strip().split()]

g = Graph(V)

for i in range(E):
    a, b = [int(i) for i in input().strip().split()]
    g.addEdge(a,b)

v1, v2 = [int(i) for i in input().strip().split()]

lst = g.dfsPath(v1, v2)
if lst:
    print(*lst)
