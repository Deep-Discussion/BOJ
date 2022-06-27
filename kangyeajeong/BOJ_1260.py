

import sys ;

N, M, V =  map(int,(input().split()));
graph = [[] for _ in range(N+1)];
    
for _ in range(M) :
    v1, v2 = map(int,(input().split()));
    graph[v1].append(v2);
    graph[v2].append(v1);

def bfs(start) :
    visit = list();
    queue = list();
    queue.append(start);

    while queue :
        node = queue.pop(0);
        if node not in visit:
            visit.append(node);
            graph[node].sort();
            queue.extend(graph[node]);
    return visit;

def dfs(start):
    visit = list();
    stack = list();
    stack.append(start);
    while stack:
        node = stack.pop();
        if node not in visit :
            visit.append(node);
            graph[node].sort(reverse=True);
            stack.extend(graph[node]);
    return visit;



d = dfs(V);
b = bfs(V);

print(*d);
print(*b);

    