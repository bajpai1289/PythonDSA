#to overcome the inefficiency of the linear storage of sata we use BST

class treeNode:
    def __init__(self,key) :
        self.key=key
        self.left=None
        self.right=None 
    def __repr__(self) -> str:
        return "key= {}, left = {}, right = {}".format(self.key,self.left,self.right)
    def __str__(self) -> str:
        return self.__repr__()

'''This is stupidest direct createion of the binnary tree        
node0=treeNode(2)
node1=treeNode(3)
node2=treeNode(5)
node3=treeNode(1)
node4=treeNode(3)
node5=treeNode(7)
node6=treeNode(4)
node7=treeNode(6)
node8=treeNode(8)
# 
node0.left=node1
node0.right=node2
node1.left=node3
node2.left=node4
node2.right=node5
node4.right=node6
node5.left=node7
node5.right=node8


# print(node0)
print(node2)

'''
tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    if isinstance(data,tuple) and len(data)==3:  #if the data is in the for m of tuple and is for length is three
        node=treeNode(data[1])
        node.left=parse_tuple(data[0])  
        node.right=parse_tuple(data[2])
    elif data is None:
        node = treeNode(data)
    else:
        node = treeNode(data)
    return node

tree2=parse_tuple(tree_tuple)
# print(tree2.left.right)


def display_keys(node,space="\t",level=0):
    #print(node.key if node else None, level)
    
    #if the node is empty
    if node is None:
        print(space*level + " ")
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space,level+1)
    
display_keys(tree2, "   ")