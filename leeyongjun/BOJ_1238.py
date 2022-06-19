import heapq
import sys

n, m, x = map(int, input().split(' '))
INF = int(1e9)
graph = [[] for _ in range(m+1)]

for _ in range(m):
    st, ed, c = map(int, sys.stdin.readline().split(' '))
    graph[st].append((ed, c))



#다익스트라 알고리즘
def dijkstra(st):
    q = []
    distance = [INF] * (m + 1)

    heapq.heappush(q, (0, st))
    distance[st] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
_out = dijkstra(x)
for i in range(1, n+1):
    _in = dijkstra(i)
    result = max(result, _in[x] + _out[i])

print(result)