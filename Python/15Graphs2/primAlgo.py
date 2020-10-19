# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the Minimum Spanning Tree (MST) using Prim's algorithm.
# For printing MST follow the steps -
# 1. In one line, print an edge which is part of MST in the format -
# v1 v2 w
# where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1 <= v2 i.e. print the smaller vertex first while printing an edge.
# 2. Print V-1 edges in above format in different lines.
# Note : Order of different edges doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# MST
# Constraints :
# 2 <= V, E <= 10^5
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 1 3
# 1 2 1
# 0 3 5

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