from collections import deque
def bfs(root):
    queue = deque()
    if root:
        queue.append(root)
    
    level = 0
    while len(queue)>0:
        print('level: ', level)
        for i in range(len(queue)):
            curr= queue.popleft()
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            level+=1

    