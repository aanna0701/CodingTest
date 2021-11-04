def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)
            
from collections import deque

def bfs(graph, node, visited):
    visited[node] = True
    queue = deque(node)
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True