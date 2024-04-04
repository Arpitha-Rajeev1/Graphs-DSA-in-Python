import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def dfs(self, sv, visited):
        visited[sv] = True

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i]:
                self.dfs(i, visited)

    def isConnected(self):
        visited = [False for i in range(self.nVertices)]
        self.dfs(0, visited)

        for boolVal in visited:
            if not boolVal:
                return False
        return True
    
arr = list(int(x) for x in stdin.readline().strip().split())
v = arr[0]
e = arr[1]
if v == 0:
    print('true')
else:
    g = Graph(v)
    for i in range(e):
        arr1 = list(int(x) for x in stdin.readline().strip().split())
        g.addEdge(arr1[0], arr1[1])

    if g.isConnected():
        print('true')
    else:
        print('false')
