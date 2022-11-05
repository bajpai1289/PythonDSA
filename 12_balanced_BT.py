def is_balanced(node):
    if node == None:
        return True , 0
    balanced_l=is_balanced(node.left)
    balanced_r=is_balanced(node.right)
    balanced=balanced_l and balanced_r and abs(hieght_l,hieght_r)<=1
    hieght=1+max(hieght_l,hieght_r)
    return balanced, hieght