from typing import List


def check_is_hole(blocks: List[int], block_idx: int):
    left_side = False
    right_side = False
    for i in range(0, block_idx):
        if blocks[i] > blocks[block_idx]:
            left_side = True
    for i in range(block_idx + 1, len(blocks)):
        if blocks[i] > blocks[block_idx]:
            right_side = True
    return left_side and right_side


def rain_water(_vh: str, _blocks: str) -> None:
    v: int
    h: int
    v, h = map(int, _vh.split())

    blocks: List[int]
    blocks = list(map(int, _blocks.split()))

    exclusive: int = max(blocks)
    total: int = 0

    if h < 3:
        return total

    for i in range(1, exclusive + 1):
        for j in range(h):
            if i > blocks[j]:
                res = check_is_hole(blocks, j)
                total += res
                blocks[j] += res
    return total


answer = rain_water(input(), input())
print(answer)