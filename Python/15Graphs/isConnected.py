# Given an undirected graph G(V,E), check if the graph G is connected graph or not.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
# Output Format :
# "true" or "false"
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3

import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        
        q.put(sv)
        visited[sv] = True
        
        while not q.empty():
            node = q.get()
            
            for i in range(self.nVertices):
                if self.adjMatrix[node][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
        
    def icConnected(self):
        visited = [False for i in range(self.nVertices)]
        self.__bfsHelper(0, visited)
        
        for i in visited:
            if i is False:
                return False
            
        return True
        
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
    
if g.icConnected():
    print('true')
else:
    print('false')
