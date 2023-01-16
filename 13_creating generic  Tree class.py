
class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None



#All the function required to the CRU operations in balanced BST
def parse_tuple(data):
    if isinstance(data,tuple) and len(data)==3:  #if the data is in the for m of tuple and is for length is three
        node=BSTNode(data[1])
        node.left=parse_tuple(data[0])  
        node.right=parse_tuple(data[2])
    elif data is None:
        node = BSTNode(data)
    else:
        node = BSTNode(data)
    return node

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
    
def is_balanced(node):
    if node == None:
        return True , 0
    balanced_l,hieght_l=is_balanced(node.left)
    balanced_r,hieght_r=is_balanced(node.right)
    balanced=balanced_l and balanced_r and abs(hieght_l,hieght_r)<=1
    hieght=1+max(hieght_l,hieght_r)
    return balanced, hieght

def make_balanced_bst(data, lo=0,hi=None, parent= None):
    if hi == None:
        hi=len(data)-1
    if lo>hi:
        return None
    mid = (lo+hi)//2
    key,value=data[mid]
    root=BSTNode(key, value)
    root.parent=parent
    root.left=make_balanced_bst(data,lo,mid-1,root)
    root.right=make_balanced_bst(data,mid+1,hi,root)
    return root
    
def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

def to_tuple(self):
    if self is None:
        return None
    if self.left is None and self.right is None:
        return self.key
    return BSTNode.to_tuple(self.left),  self.key, BSTNode.to_tuple(self.right)

def insert(node,key,value):
    if node == None:
        node=BSTNode(key, value)
    elif key<node.key:
        node.left=insert(node.left, key, value)
    
    elif key > node.key:
        node.right=insert(node.right, key, value)
        node.right.parent= node
    return node

def update(node,key, value):
    target = find(node,key)
    if target is not None:
        target.value=value
        
def list_all(node):
    if node == None:
        return []
    return list_all(node.left)+[(node.key, node.value)]+list_all(node.right)

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)



def make_balanced_bst(data, lo=0,hi=None, parent= None):
    if hi == None:
        hi=len(data)-1
    if lo>hi:
        return None
    mid = (lo+hi)//2
    key,value=data[mid]
    root=BSTNode(key, value)
    root.parent=parent
    root.left=make_balanced_bst(data,lo,mid-1,root)
    root.right=make_balanced_bst(data,mid+1,hi,root)
    return root

def balance_bst(node):
    return make_balanced_bst(list_all(node))

class treeMap:
    def __init__(self) -> None:
        self.root = None
    
    def __setitem__(self, key, value):
        node=find(self.root,key)
        if not node:
            self.root=insert(self.root, key, value)
            self.root=balance_bst(self.root)
        else:
            update(self.root, key, value)
        
    def __getitem__(self, key):
        node=find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))     #this is now a generator
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)
    
    
    
## Creating USers information

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()
    
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

treemap=treeMap()
# print(treemap)
treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh
treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal
treemap.display()


print(len(treemap))