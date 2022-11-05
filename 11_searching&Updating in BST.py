def find(node,key):
    if node is None:
        return None
    elif node.key == key:
        return node.key
    elif node.key<key:
        return find(node.right, key)
    else: return find(node.left, key)
    
    
def update(node,key, value):
    target = find(node,key)
    if target is not None:
        target.value=value
        
def list_all(node):
    if node == None:
        return []
    return list_all(node.left)+[(node.key, node.value)]+list_all(node.right)