import sys
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
        
    def minDistance(self, distance, visited):
        u = sys.maxsize
        ind = -1
        for i in range(self.nVertices):
            if visited[i] is False and distance[i] < u:
                u = distance[i]
                ind = i
        return ind
    
    def dijsktra(self):
        visited = [False]*(self.nVertices)
        distance = [sys.maxsize]*(self.nVertices)
        distance[0] = 0
        
        for i in range(self.nVertices):
            minDist = self.minDistance(distance, visited)
            visited[minDist] = True
            
            for j in range(self.nVertices):
                if self.adjMatrix[minDist][j] > 0:
                    if distance[j] > self.adjMatrix[minDist][j] + distance[minDist]:
                        distance[j] = self.adjMatrix[minDist][j] + distance[minDist]

        for i in range(self.nVertices):
            print(i, distance[i])


n, E = [int(ele) for ele in input().split()]
edges = []

g = Graph(n)
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])

g.dijsktra()