import sys

n, m, rotation = map(int, input().split(' '))
board = []

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 실버1 구현문제에 개털림.....
# 참고하였는데 다시 한번 꼮 풀어보기
for _ in range(rotation):
    for i in range(min(n, m) // 2):
        x, y = i, i
        val = board[x][y]

        for j in range(i + 1, n - i): # 좌
            x = j
            prev_value = board[x][y]
            board[x][y] = val
            val = prev_value

        for j in range(i + 1, m - i): # 하
            y = j
            prev_value = board[x][y]
            board[x][y] = val
            val = prev_value

        for j in range(i + 1, n - i): # 우
            x = n - j - 1
            prev_value = board[x][y]
            board[x][y] = val
            val = prev_value

        for j in range(i + 1, m - i): # 상
            y = m - j - 1
            prev_value = board[x][y]
            board[x][y] = val
            val = prev_value

for i in board:
    print(*i)