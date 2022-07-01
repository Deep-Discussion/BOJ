from typing import List


def digit_triangle(n: int, numbers: List[List[int]]) -> None:
    d = [[0] * (n + 1) for _ in range(n + 1)]
    d[1][1] = numbers[0][0]
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            d[i][j] = max(d[i - 1][j] + numbers[i - 1][j - 1], d[i - 1][j - 1] + numbers[i - 1][j - 1])
    print(max(d[-1]))

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
digit_triangle(N, arr)