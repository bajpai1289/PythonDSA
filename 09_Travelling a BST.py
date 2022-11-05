class treeNode:
    def __init__(self,key ):
        self.key=key
        self.right = None
        self.left = None
    def __repr__(self) -> str:
        return "node={} right={} left={}".format(self.node,self.right,self.left)
    def __str__(self) -> str:
        return self.__repr__()
    

def parse_tuple(data):
    if isinstance(data, tuple) and len(data)==3:
        node =treeNode(data[1])
        node.left=parse_tuple(data[0])
        node.right=parse_tuple(data[2])
    elif data is None:
        node=treeNode(data)
    else:
        node=treeNode(data)
    return node
        
tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))
tree=parse_tuple(tree_tuple)
# print(tree)
def traverse_inOrder(node):
    if node is None:
        return []
    return(traverse_inOrder(node.left)+[node.key]+traverse_inOrder(node.right))

def traverse_preOrder(node):
    if node == None:
        return []
    return [node.key]+traverse_preOrder(node.left)+traverse_preOrder(node.right)

def traverse_postOrder(node):
    if node==None:
        return []
    return traverse_postOrder(node.left)+traverse_postOrder(node.right)+[node.key]

print(traverse_inOrder(tree),traverse_preOrder(tree),traverse_postOrder(tree))