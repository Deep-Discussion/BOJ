from typing import List


def no_decrement(n: int) -> List[List[int]]:
    d = [[x for x in range(10, 0, -1)] for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(10):
            d[i][j] = sum(d[i - 1][j:])
    return d
    
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

result = no_decrement(max(arr))
for num in arr:
    print(result[num][0])
