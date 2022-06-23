import sys
from copy import deepcopy
from itertools import permutations
from typing import List

input = sys.stdin.readline


def array_rotation(n: int, m: int, k: int, _array: List[List[int]], rotation_info: List[List[int]]) -> None:
    answer = 1e9
    p = list(permutations(rotation_info))

    for q in p:
        array = deepcopy(_array)

        for i in range(k):
            row, col, s = q[i]
            row -= 1
            col -= 1
            for j in range(s, 0, -1):

                temp = array[row - j][col + j]
                array[row - j][col - j + 1: col + j + 1] = array[row - j][col - j: col + j]  # →

                for r in range(row - j, row + j):  # ↑
                    array[r][col - j] = array[r + 1][col - j]
                array[row + j][col - j: col + j] = array[row + j][col - j + 1: col + j + 1]  # ←

                for r in range(row + j, row - j, -1):  # ↓
                    array[r][col + j] = array[r - 1][col + j]
                array[row - j + 1][col + j] = temp  # fill the empty place on the top right corner

        for i in range(n):
            answer = min(answer, sum(array[i]))

    print(answer)
N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
info = []
for _ in range(K):
    info.append(list(map(int, input().split())))
array_rotation(N, M, K, arr, info)