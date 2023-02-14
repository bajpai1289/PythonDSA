class Tree:
    def __init__(self, root, left = None, right = None) -> None:
        self.root= root
        self.left = left
        self.right = right
    
def display(node, space = '\t', level = 0):
    if node is None:
        print(space*level+ ' ')
        return 
    if node.left is None and node.right is None:
        print(space*level+ str(node.root))
        return
    
    display(node.right, space, level+1)
    print(space*level+ str(node.root))
    display(node.left, space, level+1)
        

def parse_tuple(data):
    if isinstance(data, tuple) and len(data)==3:
        node= Tree(data[1])
        node.left = parse_tuple(data[0])
        node.right= parse_tuple(data[2])
    elif data is None:
        node = Tree(data)
    else:
        node = Tree(data)
    return node

def isSymmetric(node: Tree):
    def isSame(leftroot, rightroot):
        if leftroot is None and rightroot is None:
            return True
        elif leftroot is None or rightroot is None or leftroot.root!=rightroot.root:
            return False
        return isSame(leftroot.left, rightroot.right) and isSame(leftroot.right, rightroot.left)
    return isSame(node.left, node.right)





tree=parse_tuple(((None,2,3),1,(None,2,3)))
print(isSymmetric(tree))
a=int()
print(a)