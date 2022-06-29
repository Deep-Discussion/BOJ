from typing import List


def block_game(n: int, k: int, array: List[int]) -> int:
    answer = n
    for i in range(n):
        temp = 0
        for j in range(n):
            current = k * (j - i) + array[i]

            if current < 1:
                temp = n
                break
            if array[j] != current:
                temp += 1
        answer = min(answer, temp)

    return answer

N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(block_game(N, K, arr))