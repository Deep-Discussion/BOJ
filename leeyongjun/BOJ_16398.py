#크루스칼 알고리즘을 이용한 최소비용 신장트리 구현
import sys
input = sys.stdin.readline

#특정 우너소가 속한 집합을 찾기
def find_parent(x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n)] # 부모 테이블 초기화 (부모를 자기 자신으로 초기화)
graph = [list(map(int, input().split())) for _ in range(n)]
edges = []

#모든 간선에 대한 정보 입력 받기
for a in range(n):
    for b in range(a + 1, n):
        #비용순 정렬을 위해서 value 값을 맨 앞으로 둔다.
        edges.append((graph[a][b], a, b))

#간선을 비용순으로 정렬
edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)