import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def __bfsHelper(self, sv, v2, parentDict, visited):
        q = queue.Queue()
        found = False
        q.put(sv)
        visited[sv] = True
        
        while not q.empty():
            node = q.get()
            
            for i in range(self.nVertices):
                if self.adjMatrix[node][i] > 0 and visited[i] is False:
                    parentDict[i] = node
                    if i == v2:
                        found = True
                        break
                    q.put(i)
                    visited[i] = True
                    
            if found:
                break
        
        if found is False:
            return None
        
        address = [v2]
        val = parentDict.get(v2)
        
        while val is not None:
            address.append(val)
            val = parentDict.get(val)
            
        return address
        
        
    def bfsPath(self, v1, v2):
        parentDict = {}
        visited = [False]*(self.nVertices)
        ans = self.__bfsHelper(v1, v2, parentDict, visited)
        return ans
        
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
if V == 0 or E == 0:
    exit(0)

g = Graph(V)

for i in range(E):
    a, b = [int(i) for i in input().strip().split()]
    g.addEdge(a,b)

v1, v2 = [int(i) for i in input().strip().split()]
ans = g.bfsPath(v1, v2)

if ans:
    print(*ans)
