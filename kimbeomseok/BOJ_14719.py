from typing import List


def rain_water(_vh: str, _blocks: str) -> None:
    v: int
    h: int
    v, h = map(int, _vh.split())

    blocks: List[int]
    blocks = list(map(int, _blocks.split()))
    total: int = 0

    if h < 3:
        print(total)
        return

    for j in range(1, h - 1):
        lhs, rhs = 0, 0
        lhs, rhs = max(blocks[:j]), max(blocks[j + 1:])
        level = min(lhs, rhs)
        temp = level - blocks[j]
        if 0 < temp:
            total += temp
    print(total)


rain_water(input(), input())
