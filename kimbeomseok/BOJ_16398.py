from typing import List


def find(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: List[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def planet_connection(n: int, _planets: List[str]) -> None:
    planets = [list(map(int, x.split())) for x in _planets]
    minimum_flow = 0
    edges = []
    parent = [x for x in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            edges.append((planets[i][j], i, j))
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            minimum_flow += cost

    print(minimum_flow)


N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
planet_connection(N, arr)
