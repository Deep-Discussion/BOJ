import sys

n = int(input())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

ans = []
cnt = 0


def dfs(y, x):
    global cnt
    board[y][x] = 0
    cnt += 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for i in range(4):
        _y = dy[i] + y
        _x = dx[i] + x

        if 0 <= _y < n and 0 <= _x < n:
            if board[_y][_x] == 1:
                dfs(_y, _x)


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
for apt in ans:
    print(apt)

