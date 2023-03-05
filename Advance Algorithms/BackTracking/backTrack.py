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

def tracePath(root , path:'list' = []):
    if not root or root.val ==0:
        return False
    path.append(root.val)
    if root.left is None and root.right is None:
        return True
    if tracePath(root.left, path):
        return True
    if tracePath(root.right, path):
        return True
    return False