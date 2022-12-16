class Tree:
    def __init__(self, root) -> None:
        self.root = root
        self.left = None
        self.right = None

    def display(self, space='\t', level = 0):
        if self is None:
            print(space*level + " ")
            return
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
        
        self.display(self.right, space, level+1)
        print(space*level + str(self.key))
        self.display(self.left,space,level+1)

    def parse_tuple(self, tpl):
        if isinstance(tpl,tuple) and len(tpl)==3:
            node = Tree(tpl[1])
            node.left= Tree(tpl[0])
            node.right = Tree(tpl[2])
        
        elif tpl is None:
            node = Tree(tpl)
        else:
            return node

tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))

tree=Tree()