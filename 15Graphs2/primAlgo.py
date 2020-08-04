import sys
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
    
    def __get_minVertex(self, visited, weight):
        min_vertex = -1
        for i in range(self.nVertices):
            if (visited[i] is False and (min_vertex == -1 or weight[min_vertex] > weight[i])):
                min_vertex = i
        
        return min_vertex
    
    def prims(self):
        visited = [False]*(self.nVertices)
        parent = [-1]*(self.nVertices)
        weight = [sys.maxsize]*(self.nVertices)
        
        for i in range(self.nVertices):
            min_vertex = self.__get_minVertex(visited, weight)
            visited[min_vertex] = True
            
            # Explore neighbours of minVertes which are't visited and
            # update the weight corresponding to them if required
            
            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j] > 0 and visited[j] is False:
                    if weight[j] > self.adjMatrix[min_vertex][j]:
                        weight[j] = self.adjMatrix[min_vertex][j]
                        parent[j] = min_vertex
            
        for i in range(1, self.nVertices):
            if i < parent[i]:
                print(i, parent[i], weight[i])
            else:
                print(parent[i], i, weight[i])
                

n, E = [int(ele) for ele in input().split()]
edges = []

g = Graph(n)
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])

g.prims()