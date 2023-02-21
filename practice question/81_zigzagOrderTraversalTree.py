class Node:
    def __init__(self, val) -> None:
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self) -> None:
        self.root=None
    
    def parseTuple(self, data):
        if isinstance(data,tuple) and len(data)==3:
            self.root=Node(data[1])
            self.root.left=self.parseTuple(data[0])
            self.root.right=self.parseTuple(data[2])
        elif data is None:
            self.root = Node(data)
        else:
            self.root=Node(data)
    
    def display(self, space='/t', level=0):
        if self.root is None:
            print(space*level + " ")
            return 
    
        if self.root.left is None and self.root.right is None:
            print(space*level+ str(self.root.val))
            return
        self.display(self.root.right, space, level+1)
        print(space*level + str(self.root.val))
        self.display(self.root.right,space,level+1)


tree=Tree()
tree.parseTuple((9,3,(15,20,7)))    
tree.display()