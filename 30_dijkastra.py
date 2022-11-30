class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False) -> None:
        self.num_nodes=num_nodes
        self.directed=directed
        self.weighted=weighted
        self.data=[[] for _ in range(num_nodes)]
        self.weights=[[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                n1,n2,w=edge
                self.data[n1].append(n2)
                self.weights[n1].append(w)
                if not self.directed:
                    self.data[n2].append(n2)
                    self.weights[n2].append(w)
            
            else:
                n1,n2=edge
                self.data[n1].append(n2)
                if not directed:
                    self.data[n2].append(n1)

    def __repr__(self) -> str:
        result=""
        if self.weighted:
            for i,(node,weight) in enumerate(zip(self.data,self.weights)):
                result+="{}: {}\n".format(i,list(zip(node,weight)))
        else:
            for i,node in enumerate(self.data):
                result+="{}: {}\n".format(i, node)
        return result

    def __str__(self) -> str:
        return self.__repr__()

nodes=6
edges=[(0,1,4),(0,2,2),(1,3,10),(1,2,5),(2,4,3),(3,5,11),(4,3,4)]
graph1=Graph(nodes,edges,True,True)
# print(graph1)

def update_distances(graph,current,distance,parent):
    pass




def shortest_path(graph,source,target):
    visited=[False]*len(graph.data)
    parent=[False]*len(graph.data)  #to track the path by tracking why the node got appended in the queue
    distance=[float('inf')]*len(graph.data)
    queue=[]

    distance[source]=0
    queue.append(source)
    idx=0

    while idx<len(queue) and not visited[target]:
        current = queue[idx]
        visited[current]=True
        idx+=1
        update_distances(graph, current, distance)
        next_node=pick_next_node(distance,visited)
        if next_node:
            queue.append(next_node)

    return distance[target]