from collections import deque
class Graph:
    def __init__(self, num_nodes: int, edges: list[tuple[int]]) -> None:
        self.num_nodes=num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        
    def bfs(self, root):
        q = []
        discovered = [False]*len(self.data)
        discovered[root] = True
        q.append(root)
        idx = 0
        while idx<len(q):
            current = q[idx]
            idx+=1
            for node in self.data[current]:
                if not discovered[node]:
                    discovered[node]=True
                    q.append(node)
        return q


    def __repr__(self) -> str:
        return "\n".join(["{}: {}".format(n, niegbors) for n, niegbors in enumerate(self.data)])
    

g1 = Graph(5,[(0,1),(0,2),(1,2),(1,4),(1,3),(2,4),(3,4)])

print(g1.bfs(3))