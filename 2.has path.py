from sys import stdin

class Graph:

    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __helper(self, s, d, visited):
        if s < self.nVertices and d < self.nVertices and self.adjMatrix[s][d] > 0:
            return True

        visited[s] = True
        for i in range(self.nVertices):
            if self.adjMatrix[s][i] > 0 and visited[i] is False:
                if(self.__helper(i, d, visited)):
                    return True

        return False

    def isReachable(self, s, d):
        visited = [False for i in range(self.nVertices)]
        return self.__helper(s, d, visited)

arr = list(int(x) for x in stdin.readline().strip().split())
v = arr[0]
e = arr[1]
g = Graph(arr[0])
for i in range(e):
    arr1 = list(int(x) for x in stdin.readline().strip().split())
    g.addEdge(arr1[0], arr1[1])
arr2 = list(int(x) for x in stdin.readline().strip().split())
v1 = arr2[0]
v2 = arr2[1]
if g.isReachable(v1, v2):
    print('true')
else:
    print('false')
