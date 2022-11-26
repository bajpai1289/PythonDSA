# representing graph drawn in notebook
num_nodes=5 #number of nodes
edges=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

#to create a list of empty list 
# test_list = [[] for _ in range(10)]

#Using adjacency list to represent a graph
class Graph:
    def __init__(self, num_nodes, edges) -> None:
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            #insert into right list
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self) -> str:
        return "\n".join(["{}: {}".format(n,neighbors) for n,neighbors in enumerate(self.data)])
    
    def __str__(self):
        return self.__repr__()

graph1=Graph(num_nodes,edges)
# print(graph1)

'''Challange 1 :
Q.write a function to add an edge to a grap represented as an adjacency matrix
!. write a function to remove an edge from a graph represented as an adjacency matrix'''

def add_edge(graph, tpl):
    n1,n2=tpl
    if n1 not in graph.data[n2] and n2 not in graph.data[n1]:
        graph.data[n2].append(n1)
        graph.data[n1].append(n2)
    else:
        print('this edge already exist')
        return

def remove_edge(graph,tpl):
    n1,n2=tpl
    if n1 not in graph.data[n2] and n2 not in graph.data[n1]:
        print("no such edge exist")
        return
    graph.data[n1].remove(n2)
    graph.data[n2].remove(n1)

# add_edge(graph1,(0,1))
# print(graph1)
# remove_edge(graph1,(0,3))
# print(graph1)

#Creating an adjacency matrix 
class Adj_matrix:
    def __init__(self,num_nodes, edges) -> None:
        self.num_nodes=num_nodes
        self.data=[[0 for _ in range(num_nodes)] for x in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1][n2]=1
            self.data[n2][n1]=1
    def __repr__(self) -> str:
        return "\n".join(f"{i}" for i in self.data)
    def __str__(self) -> str:
        return self.__repr__()
        
        
        
graph2=Adj_matrix(num_nodes,edges)
print(graph2)
