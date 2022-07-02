from bisect import bisect_left
from collections import defaultdict
from typing import List, Tuple


def draw_arrow(n: int, points: List[Tuple[int]]) -> None:
    repo = defaultdict(list)
    answer = 0

    for i in range(n):
        location, color = points[i]
        repo[color].append(location)

    for k in repo.keys():
        repo[k].sort()

    for i in range(n):
        location, color = points[i]

        pivot = bisect_left(repo[color], location)
        current = repo[color][pivot]

        if pivot == 0:
            answer += abs(current - repo[color][pivot + 1])
        elif pivot == len(repo[color]) - 1:
            answer += abs(current - repo[color][pivot - 1])
        else:
            smaller = repo[color][pivot - 1]
            bigger = repo[color][pivot + 1]

            if current - smaller < bigger - current:
                answer += current - smaller
            else:
                answer += bigger - current

    print(answer)
