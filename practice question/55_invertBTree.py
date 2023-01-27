class Node:
    def __init__(self, key=None) -> None:
        self.left = None
        self.right = None
        self.key = key
    
    def parse_tuple(self, data):
        if data is None:
            node=None
        if isinstance(data, tuple) and len(data)==3:
            node=Node(data[1])
            node.left = self.parse_tuple(data[0])
            node.right = self.parse_tuple(data[2])
        else:
            node=Node(data)
        return node


    def display(self, space='/t', level=0):
        if self.key is None:
            print( space*level+ " ")
            return 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
        self.right.display()
        print(space*level + ' ')
        self.left.display()

tree1 = Node()
tree1.parse_tuple((1,2,3))
print(tree1.key, tree1.left, tree1.right)
tree1.display()