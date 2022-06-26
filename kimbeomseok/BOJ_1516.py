from collections import deque
from typing import Any, List, Tuple


def init_settings(n: int, buildings: List[List[int]]) -> Tuple[List[int], List[int], List[Any]]:

    times = [0 for _ in range(n)]
    indegrees = [0 for _ in range(n)]
    matrix: List[Any] = [[] for _ in range(n)]

    for i in range(n):
        times[i] = buildings[i][0]

        for j in range(1, len(buildings[i])):
            required_building_idx = buildings[i][j] - 1

            indegrees[i] += 1
            matrix[required_building_idx].append(i)

    return times, indegrees, matrix


def game_development(n: int, _buildings: List[str]) -> List[int]:
    buildings = [list(map(int, x.split()))[:-1] for x in _buildings]
    times: List[int]
    indegrees: List[int]
    graph: List[Any]
    times, indegrees, graph = init_settings(n, buildings)
    queue = deque([idx for idx in range(n) if indegrees[idx] == 0])

    answer = times[:]

    while queue:

        current_idx = queue.popleft()
        for building_idx in graph[current_idx]:

            answer[building_idx] = max(answer[building_idx], answer[current_idx] + times[building_idx])

            indegrees[building_idx] -= 1
            if indegrees[building_idx] <= 0:
                queue.append(building_idx)

    return answer
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
for answer in game_development(n, arr):
    print(answer)