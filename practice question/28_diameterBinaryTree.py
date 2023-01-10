class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data)==3:
            node = Tree(data[1])
            node.left = Tree.parse_tuple(data[0])
            node.right = Tree.parse_tuple(data[2])
        else:
            node = Tree(data)
        return node

    def display_keys(node,space="\t",level=0):
#print(node.key if node else None, level)

#if the node is empty
        if node is None:
            print(space*level + " ")
            return
        if node.left is None and node.right is None:
            print(space*level + str(node.value))
            return

        Tree.display_keys(node.right, space, level+1)
        print(space*level + str(node.value))
        Tree.display_keys(node.left,space,level+1)



tree=Tree.parse_tuple(((4,2,5),1,3))
# tree=Tree.parse_tuple(((1,3, None),2,(None, 4, 5)))
print("your tree: ")
tree.display_keys()

def diameterOfBinaryTree(root):
    actualroot=root
    if root is None:
        return 0
    diameter = 0
    while root is not None:
        root=root.left
        diameter+=1
    while actualroot is not None:
        actualroot=actualroot.right
        diameter+=1
    return diameter-1
print("your answer: ")
print(diameterOfBinaryTree(tree))
