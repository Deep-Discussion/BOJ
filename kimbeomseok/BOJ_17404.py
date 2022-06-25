from typing import List


def rgb_distance(n: int, _colors: List[List[int]]) -> None:
    """
    처음과 마지막이 같지 않기 위하려면 둘중에 하나를 고정시켜놓고 돌려보면 되므로 이를 정리하면 아래와 같다.
    1. 1번집이 R이고 마지막집이 R일때 최소비용
    2. 1번집이 R이고 마지막집이 G일때 최소비용
    3. 1번집이 R이고 마지막집이 B일때 최소비용
    4. 1번집이 G이고 마지막집이 R일때 최소비용
    5. 1번집이 G이고 마지막집이 G일때 최소비용
    6. 1번집이 G이고 마지막집이 B일때 최소비용
    7. 1번집이 B이고 마지막집이 R일때 최소비용
    8. 1번집이 B이고 마지막집이 G일때 최소비용
    9. 1번집이 B이고 마지막집이 B일때 최소비용
    위 항목중 1, 5, 9만을 제외한 나머지 중에서 최소비용을 찾아본다.
    """

    colors = [[0, 0, 0]] + _colors
    answer = 1e9

    for start in range(3):

        d = [[0, 0, 0] for _ in range(n + 1)]
        for j in range(3):
            if j == start:
                d[1][start] = colors[1][start]
            else:
                d[1][j] = 1e9

        for k in range(2, n + 1):
            d[k][0] = min(d[k - 1][1], d[k - 1][2]) + colors[k][0]
            d[k][1] = min(d[k - 1][0], d[k - 1][2]) + colors[k][1]
            d[k][2] = min(d[k - 1][1], d[k - 1][0]) + colors[k][2]

        for i in range(3):
            if i == start:
                continue
            answer = min(answer, d[n][i])
    print(answer)


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

rgb_distance(N, arr)