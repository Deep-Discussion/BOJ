from typing import List


def init_weight(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    if char.isupper():
        return ord(char) - 38
    return 0


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


def help_the_poor(size: int, cables: List[str]) -> None:
    edges = []
    total_weight = 0
    minimum_spanning_tree = []

    parent = [0] * (size + 1)  # 부모 테이블 초기화하기
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, size + 1):
        parent[i] = i

    for i in range(size):
        for j in range(size):
            weight = init_weight(cables[i][j])
            if weight != 0:
                edges.append((weight, i, j))
                total_weight += weight

    edges.sort()
    minimum_weight = 0

    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            minimum_weight += cost
            minimum_spanning_tree.append(edge)

        if len(minimum_spanning_tree) == size - 1:
            break

    if len(minimum_spanning_tree) < size - 1:
        print(-1)
        return
    else:
        print(total_weight - minimum_weight)


n = int(input())
help_the_poor(n, [input() for _ in range(n)])
