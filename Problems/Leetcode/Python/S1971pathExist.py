from collections import deque


class Solution:
    def validPath(self, n, edges, source, destination) -> bool:
        if source == destination:
            return True
        graph = dict()

        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False]*n

        dq = deque([source])

        while dq:
            node = dq.popleft()

            for nbr in graph[node]:
                if nbr == destination:
                    return True
                elif not visited[nbr]:
                    visited[nbr] = True
                    dq.append(nbr)
        return False


n_vertices = int(input())
n_edges = int(input())
edges = [[int(i) for i in input().split()] for j in range(n_edges)]
sources = int(input())
destination = int(input())

ob = Solution()
print(ob.validPath(n_vertices, edges, sources, destination))
