def canReachLeaf(root):
    if not root or root.value ==0:
        return False
     
    if root.left is None and root.right is None:
        return True
    
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False