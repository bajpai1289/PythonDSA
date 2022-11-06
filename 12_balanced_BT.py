def is_balanced(node):
    if node == None:
        return True , 0
    balanced_l=is_balanced(node.left)
    balanced_r=is_balanced(node.right)
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
    root=BSTnode(key, value)
    root.parent=parent
    root.left=make_balanced_bst(data,lo,mid-1,root)
    root.right=make_balanced_bst(data,mid+1,hi,root)
    return root