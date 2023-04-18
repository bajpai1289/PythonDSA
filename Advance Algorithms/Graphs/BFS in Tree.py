from collections import deque
class Node:
    def __init__(self, val: int) -> None:
        self.value=val
        self.left = None
        self.right = None


def parse_tuple( tpl: tuple):
    if isinstance(tpl , tuple) and len(tpl)==3:
        root=Node(tpl[1])
        root.left=parse_tuple(tpl[0])
        root.right = parse_tuple(tpl[2])
    elif tpl is None:
        root = Node(tpl)
    else:
        root = Node(tpl)
    return root
        
def show(root: 'Node', space='\t', level = 0):
    if root is None:
        print(space*level+" ")
        return 
    if root.left is None and root.right is None:
        print(space*level+ str(root.value))
        return 
    show(root.left, space="\t",level=level+1)
    print(space*level+ str(root.value))
    show(root.right, space, level+1)

def bfs( root: Node):
    queue: deque[Node] = deque()
    if root: 
        queue.append(root)
    level = 0
    while len(queue)>0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            level+=1



# tree = Node()
# print(tree.root)
# tree.parse_tuple((4,3,1))
# show(tree)
tree = parse_tuple((4,3,1))
show(tree)
bfs(tree)