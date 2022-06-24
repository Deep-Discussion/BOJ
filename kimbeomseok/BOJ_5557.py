from typing import List




def first_grade(n: int, numbers: List[int]) -> None:
    d = [[0] * 21 for _ in range(n)]
    is_valid_range = lambda x: 0 <= x <= 20

    d[0][numbers[0]] = 1
    for i in range(1, n - 1):
        for j in range(21):
            if 0 < d[i-1][j]:
                plus = j + numbers[i]
                minus = j - numbers[i]
                
                if is_valid_range(plus):
                    d[i][j + numbers[i]] += d[i-1][j]
                if is_valid_range(minus):
                    d[i][j - numbers[i]] += d[i-1][j]
    print(d[n-2][numbers[-1]])
N = int(input())
numbers = list(map(int, input().split()))
first_grade(N, numbers)
