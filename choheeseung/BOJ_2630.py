# 분할정복

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

blue = 0
white = 0


def solution(x, y, n):
    global blue, white
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:  # 전체 종이가 모두 같은 색으로 칠해져 있지 않으면
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


solution(0, 0, n)
print(white)
print(blue)
