import itertools
import sys
from typing import Dict, Iterable, List

input = sys.stdin.readline



def exchange_xy(array: Iterable[List[int]]) -> List[List[int]]:
    return list(itertools.zip_longest(*array, fillvalue=0))


def extract(array: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(len(array)):
        counter: Dict[int, int] = {}
        for j in range(len(array[0])):
            if array[i][j] == 0:
                continue
            counter[array[i][j]] = counter.get(array[i][j], 0) + 1

        repo = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        extracted = []
        for item in repo:
            a, b = item
            extracted.extend([a, b])
        result.append(extracted)
    return result


def update(data: List[List[int]]) -> List[List[int]]:
    updated = []
    max_length = len(max(data, key=lambda x: len(x)))

    for i in range(len(data)):
        length = len(data[i])
        updated.append(data[i] + [0] * (max_length - length))
    return updated


def two_dimensional_operation(r: int, c: int, k: int, array: List[List[int]]) -> None:
    count = 0

    while True:

        if count > 100:
            count = -1
            break
        try:
            if array[r - 1][c - 1] == k:
                break
        except IndexError:
            pass

        row_length = len(array)
        col_length = len(array[0])

        if row_length < col_length:
            array = exchange_xy(array)

        array = update(extract(array))
        if row_length < col_length:
            array = exchange_xy(array)

        count += 1
    print(count)



R, C, K = map(int, input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
two_dimensional_operation(R, C, K, arr)
