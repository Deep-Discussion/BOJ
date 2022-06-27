from copy import deepcopy
from typing import List, Tuple


def find_clean_machine(n: int, matrix: List[List[int]]) -> Tuple:
    start = 0
    for row in range(n):
        if matrix[row][0] == -1:
            start = row
            break

    return start, start + 1


def spread(r, c, result, spreaded, divided, machine_row_1, machine_row_2) -> Tuple[List[List[int]], List[List[int]]]:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for x in range(r):
        for y in range(c):
            if (x, y) == (machine_row_1, 0) or (x, y) == (machine_row_2, 0):
                result[x][y] = 0
                continue

            spreaded_amount = result[x][y] // 5
            spreaded_count = 0

            for z in range(4):
                nx, ny = x + dx[z], y + dy[z]
                if not (0 <= nx < r and 0 <= ny < c):
                    continue
                if (nx, ny) == (machine_row_1, 0) or (nx, ny) == (machine_row_2, 0):
                    continue
                spreaded[nx][ny] += spreaded_amount
                spreaded_count += 1

            divided[x][y] = result[x][y] - spreaded_amount * spreaded_count
    return divided, spreaded


def work(r, c, result, machine_row_1, machine_row_2) -> List[List[int]]:
    temp = result[machine_row_1][c - 1]
    result[machine_row_1][1:c] = result[machine_row_1][0:c - 1]  # 우
    for i in range(machine_row_1, 0, -1):  # 하
        result[i][0] = result[i - 1][0]
    result[0][0: c - 1] = result[0][1: c]  # 좌
    for i in range(0, machine_row_1):  # 상
        result[i][c - 1] = result[i + 1][c - 1]
    result[machine_row_1 - 1][c - 1] = temp

    temp2 = result[machine_row_2][c - 1]
    result[machine_row_2][1:c] = result[machine_row_2][0: c - 1]  # 우
    for i in range(machine_row_2, r - 1):  # 상
        result[i][0] = result[i + 1][0]
    result[r - 1][0: c - 1] = result[r - 1][1:c]  # 좌
    for i in range(r - 1, machine_row_2, -1):  # 하
        result[i][c - 1] = result[i - 1][c - 1]
    result[machine_row_2 + 1][c - 1] = temp2
    return result


def good_by_pm(r: int, c: int, t: int, matrix: List[List[int]]) -> None:
    spreaded = [[0] * c for _ in range(r)]
    divided = [[0] * c for _ in range(r)]
    empty_matrix = [[0] * c for _ in range(r)]

    result = matrix[:]
    machine_row_1, machine_row_2 = find_clean_machine(r, matrix)
    result[machine_row_1][0] = 0
    result[machine_row_2][0] = 0

    for _ in range(t):
        divided, spreaded = spread(r, c, result, spreaded, divided, machine_row_1, machine_row_2)
        updated = deepcopy(empty_matrix)
        for x in range(r):
            for y in range(c):
                updated[x][y] = divided[x][y] + spreaded[x][y]

        result = work(r, c, updated, machine_row_1, machine_row_2)
        result[machine_row_1][0] = 0
        result[machine_row_2][0] = 0
        divided = deepcopy(empty_matrix)
        spreaded = deepcopy(empty_matrix)

    answer = 0
    for idx in range(r):
        total = sum(result[idx])
        answer += total
    print(answer)
