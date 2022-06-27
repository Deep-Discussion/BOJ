import sys
from typing import List
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def get_areas(m: int, n: int, k: int, squares: List[List[int]]) -> None:
    count = 0
    area_count = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    field = [[0] * n for _ in range(m)]

    for square in squares:
        y1, x1, y2, x2 = square
        for i in range(x1, x2):
            for j in range(y1, y2):
                field[i][j] = 1

    def search(x: int, y: int, c: int) -> int:
        nonlocal field, dx, dy, m, n
        field[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < m and 0 <= ny < n) or field[nx][ny] == 1:
                continue
            c += search(nx, ny, 0) + 1

        return c

    for i in range(m):
        for j in range(n):
            if field[i][j] == 0:
                count += 1
                area_count.append(search(i, j, 1))
    print(count)
    print(*sorted(area_count))

M, N, K = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(list(map(int, input().split())))
get_areas(M, N, K, arr)
