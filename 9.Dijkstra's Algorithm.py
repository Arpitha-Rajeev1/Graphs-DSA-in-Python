class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		for node in range(self.V):
			print(node, "\t\t", dist[node])

	def addEdge(self, v1, v2, wt):
		self.graph[v1][v2] = wt
		self.graph[v2][v1] = wt

	def minDistance(self, dist, sptSet):
		min = 1e7

		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			u = self.minDistance(dist, sptSet)

			sptSet[u] = True

			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]

g = Graph(n)
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])

g.dijkstra(0)

