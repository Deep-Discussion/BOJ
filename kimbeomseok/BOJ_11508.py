from typing import List


def two_plus_one_sale(n: int, _milks: List[int]) -> None:
    milks = sorted(_milks, reverse=True)
    cost = 0

    for i in range(0, n, 3):
        if n <= i + 1 or n <= i + 2:
            cost += sum(milks[i:])
            break
        idx1, idx2 = i, i + 1
        milk1, milk2 = milks[idx1], milks[idx2]
        cost += milk1 + milk2
    print(cost)


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
two_plus_one_sale(n, arr)
