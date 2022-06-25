from copy import deepcopy
from typing import List


def n_queen(n: int) -> None:
    dx = [-1, -1, -1]
    dy = [-1, 0, 1]
    board = [[0] * n for _ in range(n)]
    ans = 0

    def check_is_valid_direction(x: int, y: int, d_num: int, board: List[List[int]]) -> bool:
        nonlocal n

        if not (0 <= x < n and 0 <= y < n):
            return True

        if board[x][y] == 1:
            return False

        return check_is_valid_direction(x + dx[d_num], y + dy[d_num], d_num, board)

    def solve(board: List[List[int]], x: int, y: int, c: int) -> bool:
        nonlocal ans, n

        nx = x + 1
        if nx == n:
            ans += 1
            return

        for i in range(n):
            if y == i or y - 1 == i or y + 1 == i:
                continue

            is_valid = True
            for j in range(3):

                if not check_is_valid_direction(nx, i, j, board):
                    is_valid = False

            if is_valid:
                _board = deepcopy(board)
                _board[nx][i] = 1
                solve(_board, nx, i, c + 1)

    for j in range(n):
        temp = deepcopy(board)
        temp[0][j] = 1
        solve(temp, 0, j, 1)

    print(ans)
