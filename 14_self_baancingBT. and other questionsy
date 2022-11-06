#TODO:
''' 
1. Implement rotations and self balancing insertion
2. Delete a node from a binary tree
3. implement deletion with balancing
4. find the lowest common ancestor of two nodes in a tree {use parent property}
5. find the next node in a lexicographical order for a given node
6. givine the number k find the kth node in a bst

do here:
https://leetcode.com/tag/tree/
https://medium.com/techie-delight/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f

'''

class bstNode:
    def __init__(self, key, value=None):
        self.key=key
        self.value=value
        self.parent = None
        self.left=None
        self.right=None
    
def parse_tuple(tupl):
    if isinstance(tupl, tuple) and len(tupl)==3:
        node=bstNode(tupl[1])
        node.left=parse_tuple(tupl[0])
        node.right=parse_tuple(tupl[2])
    elif tupl is None:
        node=None
    else:
        node=bstNode(tupl)
    return node