from typing import List


def cal(M: int, cakes: List[int]):
    n = 0
    target_cakes = []
    indivisible_cakes = []
    divisible_cakes = []

    for cake in cakes:
        if cake == 10:
            n += 1
            continue
        if cake < 10:
            continue

        if cake % 10 == 0:
            divisible_cakes.append(cake)
        else:
            indivisible_cakes.append(cake)
    target_cakes = divisible_cakes + indivisible_cakes

    idx = 0
    cc = M
    while idx < len(target_cakes) and 0 < cc:
        if target_cakes[idx] < 10:
            idx += 1
            continue
            # 다음으로 이동

        if target_cakes[idx] == 10:
            n += 1
            target_cakes[idx] -= 10
            idx += 1
            continue
            # 10일 경우 갯수에 추가하고 다음으로 이동

        if 10 < target_cakes[idx]:
            target_cakes[idx] -= 10
            cc -= 1
            n += 1
            # 10 이상일경우 갯수에 추가하고 커팅
    if idx != len(target_cakes) and target_cakes[idx] == 10:
        n += 1

    print(n)


def roll_cake(M: int, cakes: List[int]) -> None:
    cal(M, sorted(cakes))
