import itertools
import sys
from copy import deepcopy
n, m = map(int, input().split())

board = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
points = []
ans = float('inf')

#바이러스 시작 좌표 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            points.append((i, j))



def check(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return False

    return True


def print_board(board):
    for i in range(n):
        print()
        for j in range(n):
            print(board[i][j], end=' ')
    print()


#bfs를 이용한 구현
def solution(points, num, board):
    global ans

    if check(board):
        ans = min(num, ans)
        return

    if not points:
        return

    num += 1
    new_points = []

    while points:
        y, x = points.pop()
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]

        for i in range(4):
            _y = y + dy[i]
            _x = x + dx[i]
            if 0 <= _y < n and 0 <= _x < n:
                if board[_y][_x] == 0:
                    board[_y][_x] = '*'
                    new_points.append((_y, _x))

    # print_board(board)
    solution(new_points, num, board)


_points = itertools.combinations(points, m)
for p in _points:
    _p = []
    for i in p:
        _p.append(i)
    
    new_board = deepcopy(board)
    solution(_p, 0, new_board)

if ans == float('inf'):
    print(-1)
else:
    print(ans)

