class Graph:
    def __init__(self, num_nodes, edges) -> None:
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        
    def __repr__(self) -> str:
        return "\n".join([f"{n}: {neigh}" for n, neigh in enumerate(self.data)])
    
    def __str__(self) -> str:
        return self.__repr__()


nodes=5
edg=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

graph1=Graph(nodes, edg)
# print(graph1)

def dfs(graph, root):
    stack=[]
    res=[]
    discovered = [False]*len(graph.data)
    stack.append(root)
    while len(stack)>0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current]=True
            res.append(current)

        for node in graph.data[current]:
            if not discovered[node]:
                stack.append(node)

    return res


print(dfs(graph1,3))