import sys
from typing import List

sys.setrecursionlimit(10**6)
N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_for_party(color1, color2):
    return (color1 != "B" and color2 != "B") or color1 == color2


def check_for_normal(color1, color2):
    return color1 == color2


def search(field, x, y, visited, condition):
    visited[x][y] = 1
    check = check_for_normal
    if condition == "party":
        check = check_for_party

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1:
            prev_color = field[x][y]
            cur_color = field[nx][ny]

            if check(prev_color, cur_color):
                search(field, nx, ny, visited, condition)


def red_green_color_weakness(field: List[str]) -> None:

    party = [[0 for _ in range(len(field[0]))] for _ in range(len(field))]
    normal = [[0 for _ in range(len(field[0]))] for _ in range(len(field))]
    party_count = 0
    normal_count = 0

    for i in range(len(field)):
        for j in range(len(field[0])):
            if party[i][j] == 0:
                search(field, i, j, party, "party")
                party_count += 1
            if normal[i][j] == 0:
                search(field, i, j, normal, "normal")
                normal_count += 1

    print(normal_count, party_count)


arr = []
for _ in range(N):
    n = input()
    arr.append(n)
red_green_color_weakness(arr)
