#enter the nodes and the corresponding connecting nodes
graph = {
    '0' : set(['1','2','3']),
    '1' : set(['0','2']),
    '2' : set(['0','4']),
    '3' : set(['0']),
    '4' : set(['2'])
    }

#creating function
def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n,visited)
        return visited
    
visited = dfs(graph,'0',[])     #second value for checking from required condition
print(visited)
