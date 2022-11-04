class TreeNode:
    def __init__(self,key) -> None:
        self.key,self.left,self.right=key,None,None
    
    def hieght(self):
        if self == None:
            return 0
        return 1 +max(TreeNode.hieght(self.left),TreeNode.hieght(self.right))
    
    def size(self):
        if self == None:
            return 0
        return 1 + TreeNode.size(self.left)+TreeNode.size(self.right)
    
    def inOrderTraverse(self):
        if self == None:
            return []
        return TreeNode.inOrderTraverse(self.left)+[self.key]+TreeNode.inOrderTraverse(self.right)
    
    def preOrderTraverse(self):
        if self == None:
            return []
        return [self.key]+TreeNode.preOrderTraverse(self.left+TreeNode.preOrderTraverse(self.right))
    
    def postOrderTraverse(self):
        if self == None:
            return []
        return TreeNode.postOrderTraverse(self.left)+TreeNode.postOrderTraverse(self.right)+[self.key]
    
    def __repr__(self) -> str:
        return "key= {}, left = {}, right = {}".format(self.key,self.left,self.right)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data)==3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else: node = TreeNode(data)
        return node
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    @staticmethod
    def remove_none( nums):
        return [x for x in nums if x is not None]
    
    @staticmethod
    def is_bst(node):
        if node is None:
            return True, None, None
    
        is_bst_l,min_l,max_l =TreeNode.is_bst(node.left)
        is_bst_r,min_r,max_r =TreeNode.is_bst(node.right)
    
        is_bst_node = (is_bst_l and is_bst_r and (max_l is None or node.key>max_l) and (min_r is None or node.key<max_r))
    
        min_key = min(TreeNode.remove_none([min_l, node.key, min_r]))
        max_key = max(TreeNode.remove_none([max_l, node.key, max_r]))
    
        return is_bst_node, min_key, max_key

    @staticmethod
    def display_keys(node,space="\t",level=0):
    #print(node.key if node else None, level)
    
    #if the node is empty
        if node is None:
            print(space*level + " ")
            return
        if node.left is None and node.right is None:
            print(space*level + str(node.key))
            return
    
        TreeNode.display_keys(node.right, space, level+1)
        print(space*level + str(node.key))
        TreeNode.display_keys(node.left,space,level+1)
        
    @staticmethod
    def insert(node,key):
        if node == None:
            node=TreeNode(key)
        elif key<node.key:
            node.left=TreeNode.insert(node.left, key)
        
        elif key > node.key:
            node.right=TreeNode.insert(node.right, key)
            node.right.parent= node
        return node
        

    

        
# tree = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
# TreeNode.display_keys(tree)
# print(TreeNode.is_bst(tree))

# <---------------------------    -------------------------------#

class BSTNode:
    def __init__(self,key, value = None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
    @staticmethod
    def insert(node,key,value):
        if node == None:
            node=BSTNode(key, value)
        elif key<node.key:
            node.left=BSTNode.insert(node.left, key, value)
        
        elif key > node.key:
            node.right=BSTNode.insert(node.right, key, value)
            node.right.parent= node
        return node
    
    @staticmethod
    def display_keys(node,space="\t",level=0):
    #print(node.key if node else None, level)
    
    #if the node is empty
        if node is None:
            print(space*level + " ")
            return
        if node.left is None and node.right is None:
            print(space*level + str(node.key))
            return
    
        TreeNode.display_keys(node.right, space, level+1)
        print(space*level + str(node.key))
        TreeNode.display_keys(node.left,space,level+1)
        
# tree2= BSTNode('jadhesh.username', 'jadhesh')
# print(tree2.key, tree2.value)


tree3 = BSTNode.insert(None, 'jadhesh.username', 'jadhesh')
BSTNode.insert(tree3, 'sonaksh.username', 'sonaksh')
BSTNode.insert(tree3, 'aakash.username', 'aakash')
BSTNode.insert(tree3, 'hemanth.username', 'hemanth')
BSTNode.insert(tree3, 'siddhant.username', 'siddhant')
# BSTNode.insert(tree3, 'vishal.usernamel', 'vishal')


tree4 = TreeNode.insert(None, 'jadhesh')
TreeNode.insert(tree4, 'sonaksh')
TreeNode.insert(tree4, 'aakash')
TreeNode.insert(tree4, 'hemanth')
TreeNode.insert(tree4, 'siddhant')
TreeNode.insert(tree4, 'vishal')
TreeNode.display_keys(tree4)





# def insert(node,key,value):
#     if node == None:
#         node = BSTnode(key, value)
#     elif node < node.key:
#         node.left = insert(node.left, key, value)
#         node.left.parent = node
#     elif node > node.key:
#         node.right= insert(node.right, key , value)
#         node.right.parent = node
#     return node


