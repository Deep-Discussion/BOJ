from typing import List


def coin_problem(n: int, coins: List[int], money: int) -> None:
    d = [[0 for _ in range(money + 1)] for _ in range(n)]
    for i in range(n):
        d[i][0] = 1

    for m in range(1, money + 1):
        for coin_idx in range(n):
            coin = coins[coin_idx]
            d[coin_idx][m] = d[coin_idx - 1][m]
            if 0 <= m - coin:
                d[coin_idx][m] += d[coin_idx][m - coin]
    print(d[-1][-1])

    
N = int(input())
for _ in range(N):
    coin_num = int(input())
    coin_list = list(map(int, input().split()))
    money = int(input())
    coin_problem(coin_num, coin_list, money)
