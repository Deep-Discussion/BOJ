from typing import List


def cow_burger(n: int, m: int, k: int, _orders: List[List[int]]) -> None:
    orders = [[0, 0]] + _orders
    d = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

    for order in range(1, n + 1):
        current_burger, current_potato = orders[order]
        for i in range(1, m + 1):
            for j in range(1, k + 1):
                if current_burger <= i and current_potato <= j:
                    d[order][i][j] = max(1 + d[order - 1][i - current_burger][j - current_potato],
                                         d[order - 1][i][j])
                else:
                    d[order][i][j] = d[order - 1][i][j]

    print(d[n][m][k])


N, M, K = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
cow_burger(N, M, K, arr)
