import sys
from collections import deque
from typing import Any, List, Tuple

input = sys.stdin.readline


def init_settings(n: int, k: int, buildings: List[List[int]]):
    indegrees = [0 for _ in range(n)]
    matrix = [[] for _ in range(n)]

    for j in range(k):
        x_building, y_building = buildings[j]
        x_building -= 1
        y_building -= 1
        indegrees[y_building] += 1
        matrix[x_building].append(y_building)

    return indegrees, matrix


def acm_craft(n: int, k: int, times: List[int], buildings: List[List[int]], target_building_num: int) -> None:
    indegrees, matrix = init_settings(n, k, buildings)
    queue = deque([idx for idx in range(n) if indegrees[idx] == 0])
    answer = times[:]

    while queue:
        current_idx = queue.popleft()
        for building_idx in matrix[current_idx]:
            answer[building_idx] = max(answer[building_idx], answer[current_idx] + times[building_idx])

            indegrees[building_idx] -= 1
            if indegrees[building_idx] <= 0:
                queue.append(building_idx)

    print(answer[target_building_num - 1])

for _ in range(int(input())):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    buildings = []
    for _ in range(k):
        buildings.append(list(map(int, input().split())))
    target_building_num = int(input())
    acm_craft(n, k, times, buildings, target_building_num)
        