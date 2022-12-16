class Graph:
    def __init__(self, num_nodes, edges, directed=False,weighted=False) -> None:
        self.num_nodes=num_nodes
        self.directed=directed
        self.weighted=weighted
        self.data=[[] for _ in range(num_nodes)]
        self.weights=[[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                n1, n2, w=edge
                self.data[n1].append(n2)
                self.weights[n1].append(w)
                if not self.directed:
                    self.data[n2].append(n1)
                    self.weights[n2].append(w)
            else:
                n1,n2=edge
                self.data[n1].append(n2)
                if not self.directed:
                    self.data[n2].append(n1)

    def isCyclic(self, v, visited, parent):
        # mark the current node as visited
        visited[v]=True
        for i in self:
            pass

    def __repr__(self) -> str:
        result = ""
        if self.weighted:
            for i,(node,wieght) in enumerate(list(zip(self.data,self.weights))):             
                result+="{}: {}\n".format(i,list(zip(node,wieght)))
        else:
            for i, node in enumerate(self.data):
                result+="{}: {}\n".format(i, node)
        return result

    def __str__(self) -> str:
        return self.__repr__()


node=5
edges=[(1,0),(0,2),(1,2),(0,3),(3,4)]
graph1=Graph(node,edges)
print(graph1)



# def bfs(graph, root):
#     queue=[]
#     discovered = [False]*len(graph.data)
#     idx=0
#     discovered[root]=True
#     queue.append(root)
#     while idx<len(queue):
#         current=queue[idx]
#         idx+=1
#     for node in graph.data[current]:
#         if not discovered[node]:
#             discovered[node]=True
#             queue.append(node)

#     return queue

# def bfs(graph,root):
#     queue=[]
#     discoverd=[False]*len(graph.data)
#     discoverd[root]=True
#     queue.append(root)
    
#     idx=0
#     while idx<len(queue):  #next available index is less than the length of the sequence
#         current = queue[idx]
#         idx+=1
        
#         #checking all edges of current
#         for node in graph.data[current]:
#             if not discoverd[node]:
#                 discoverd[node]=True
#                 queue.append(node)
#     return queue

# print(bfs(graph1,0))
integer=int('100111', base=2)
print(integer)