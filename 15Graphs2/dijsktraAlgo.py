# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
# Print the ith vertex number and the distance from source in one line separated by space. Print different vertices in different lines.
# Note : Order of vertices in output doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# In different lines, ith vertex number and its distance from source (separated by space)
# Constraints :
# 2 <= V, E <= 10^5
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 0
# 1 3
# 2 4
# 3 5

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