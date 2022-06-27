# python3으로 제출하면 시간초과
# pypy3로 제출하면 통과....

# n, m 은 배열 크기
# r은 회전 수
n, m, r = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(r):
    # ← ↓ → ↑

    # 가장자리 ~ 안쪽까지 돌리는 횟수
    for j in range(min(n, m) // 2):
        x, y = j, j
        value = arr[x][y]

        # 왼쪽으로
        for k in range(j + 1, n - j):
            x = k
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value

        # 아래로
        for k in range(j + 1, m - j):
            y = k
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value

        # 오른쪽으로
        for k in range(j + 1, n - j):
            x = n - k - 1
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value

        # 위로
        for k in range(j + 1, m - j):
            y = m - k - 1
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
