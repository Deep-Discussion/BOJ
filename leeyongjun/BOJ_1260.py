import collections
import sys

n, m, v = map(int, sys.stdin.readline().split())
dic = collections.defaultdict(list)

for _ in range(m):
    st, ed = map(int, input().split(' '))
    dic[st].append(ed)
    dic[ed].append(st)

for i in range(1, n+1):
    dic[i].sort()

visited = [False for _ in range(n + 1)]


def dfs(st):
    print(st, end=' ')
    visited[st] = True
    for i in dic[st]:
        if not visited[i]:
            dfs(i)
            visited[i] = True


def bfs(st):
    visited = [False for _ in range(n + 1)]
    q = collections.deque()
    q.append(st)
    visited[st] = True

    while q:
        _st = q.popleft()

        print(_st, end=' ')
        points = dic[_st]

        for point in points:
            if not visited[point]:
                visited[point] = True
                q.append(point)


dfs(v)
print()
bfs(v)