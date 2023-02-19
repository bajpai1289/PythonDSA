class Graph:
    def __init__(self, num_nodes, edges) -> None:
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        
    def __repr__(self) -> str:
        return "\n".join([f"{n}: {nieghbours}" for n,nieghbours in enumerate(self.data)])
    
    def __str__(self) -> str:
        return self.__repr__()
    
# num_nodes=5
# edges=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

# graph1=Graph(num_nodes,edges)
# print(graph1)

def bfs(graph,root):
    queue=[]
    discoverd=[False]*len(graph.data)
    discoverd[root]=True
    queue.append(root)
    
    idx=0
    while idx<len(queue):  #next available index is less than the length of the sequence
        current = queue[idx]
        idx+=1
        
        #checking all edges of current
        for node in graph.data[current]:
            if not discoverd[node]:
                discoverd[node]=True
                queue.append(node)
    return queue
# print(bfs(graph1,3))  #this will return the bfs traversal of the graph but
#if we can also keep track of the distance it would be really helpful in every case of real life problems

def bfs_with_distance_and_parent(graph,root):
    queue=[]
    discovered=[False]*len(graph.data)
    distance=[None]*len(graph.data)
    parent=[None]*len(graph.data)
    queue.append(root)
    discovered[root]=True
    distance[root]=0
    idx=0   #because pyton doensnt give me something to remove an element from the queue
    while idx<len(queue):
        current=queue[idx]
        idx+=1
        
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node]=1+distance[current]
                parent[node]=current
                discovered[node]=True
                queue.append(node)
    return queue,distance,parent

# print(bfs_with_distance_and_parent(graph1,3))


'''Challange:
To check if all the nodes in a graph are connected
example of a node where not all edges are connected:
num_nodes3=9
edges3=[(0,1),(0,3),(1,2),(2,3),(4,5),(4,6),(5,6),(7,8)]
Hint: use bfs's returned queue: the queue gives us all the nodes starting from the source node 
      are connected the to the source node if something is not connected it would not show up on the list
      so check the length of the que and see that if its less than the total number of nodes and then use that
      to detemin that if they are connected or note
      
q2. to find the number of connected components
connected compnents: if you take a set of nodes thats connected thats 1 component and when you remove 
                     that and then you look at the next set thats connected thts 2 components 
Hint: using bfs, pick up a first node, perform bfs on it that gives you the connected component of the first node
      look at 9:37:00                

'''
num_nodes3=5
edges3=[(0,1),(0,2),(2,3),(2,4)]
graph2=Graph(num_nodes3,edges3)
print(graph2)
print(bfs(graph2,0))

# node=5
# edges=[(1,0),(0,2),(1,2),(0,3),(3,4)]
# graph3=Graph(node,edges)
# print(graph3)
# print(bfs_with_distance_and_parent(graph3,0))

# num_nodes4=10
# edges4=[(0,1),(0,2),(0,3),(1,4),(2,5),(2,6),(3,9),(4,8),(6,7),(6,9),(8,9)]
# graph5=Graph(num_nodes4,edges4)
# print(graph5)
# print(bfs_with_distance_and_parent(graph5,0))