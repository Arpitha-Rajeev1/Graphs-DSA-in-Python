

class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)]for j in range(self.nVertices)]
        
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
        
    def getPathBFS(self,sv,ev):
        import queue
        q=queue.Queue()
        visited=[False for i in range(self.nVertices)]
        
        q.put(sv)
        visited[sv]=True
        parent={}
        while q.empty() is False:
            
            front=q.get()
            if front==ev:
                path=[ev]
                while ev!=sv:
                    ev=parent[ev]
                    path.append(ev)
                return path
            for i in range(self.nVertices):
                
                if self.adjMatrix[front][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
                    parent[i]=front



arr=[int(i) for i in input().strip().split()]
V=arr[0];E=arr[1]
g=Graph(V)


for i in range(E):
    arr=[int(j) for j in input().strip().split()]
    a=arr[0];b=arr[1]
    g.addEdge(a,b)
arr=[int(i) for i in input().strip().split()]

V1=arr[0];V2=arr[1]
Path=g.getPathBFS(V1,V2)


if Path is not None:
    for i in Path:
        print(i,end=" ")
