class Graph:
    def __init__(self, num_nodes,edges,directed=False, weighted=False) -> None:
        self.num_nodes=num_nodes
        self.directed=directed
        self.weighted=weighted
        self.data=[[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted==True:
                #include weights
                node1,node2,weight=edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                #work withoud weighjts
                node1,node2=edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
    
    def __repr__(self) -> str:
        result =""
        if self.weighted:
            for i,(nodes, weghts) in enumerate(zip(self.data,self.weight)):
                result+='{}: {}\n'.format(i, list(zip(nodes,weghts)))
        else:
            for i, nodes in enumerate(self.data):
                result+="{}: {}\n".format(i, nodes)
        return result
num_nodes=5 #number of nodes
edges=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
graph1=Graph(num_nodes,edges)
# print(graph1)

num_nodes2=9
edges2=[(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]

graph2=Graph(num_nodes2,edges2,directed=False, weighted=True)
# print(graph2)

nodes=5
edges6=[(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)]
dir_graph=Graph(nodes,edges6,True,False)
print(dir_graph)