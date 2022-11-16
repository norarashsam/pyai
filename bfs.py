#enter the nodes and the corresponding connecting nodes
graph = {
    'A' : (['B','C']),
    'B' : (['A']),
    'C' : (['A','F']),
    'F' : (['C'])
    }

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue :
        s = queue.pop(0)
    #print(s,end=" ")
    for n in graph[s]:
        visited.append(n)
        queue.append(n)

bfs(visited,graph,'F')
print(visited)
