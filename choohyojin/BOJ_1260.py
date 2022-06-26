from collections import deque

def DFS(graph, node, visited):
    visited[node] = True
    print(node + 1, end = " ")
    
    for i in graph[node]:
        if not visited[i]:
            DFS(graph, i, visited)
            
            
def BFS(graph, node, visited):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        v = queue.popleft()
        print(v + 1, end = " ")
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#########################

n, m, v = map(int, input().split())
# 인접 행렬 
graph = [[] for j in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)
for i in range(n):
    graph[i].sort()
    
visited = [False for i in range(n)]
DFS(graph, v - 1, visited)
print()
visited = [False for i in range(n)]
BFS(graph, v - 1, visited)
print()