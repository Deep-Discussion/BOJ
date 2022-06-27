import sys

n, m = map(int, (input().split(' ')))

guitars = [sys.stdin.readline().rsplit() for _ in range(n)]
used = ''
ans = float('inf')
cnt = 0
for i in range(n):
    guitars[i][1] = list(guitars[i][1])

## or 연산을 통해서 y가 하나라도 있으면 y로 바꿔줌
def _or(l1, l2):
    _l = ['N' for _ in range(m)]

    for i in range(m):
        if l1[i] == 'Y' or l2[i] == 'Y':
            _l[i] = 'Y'

    return _l

# 연주가능한 수 출력
def count_y(l):
    c = 0
    for _l in l:
        if _l == 'Y':
            c += 1
    return c

# 백트래킹을 통해서 완전탐색
def search(l, index, num):
    global ans, cnt
    total_y = count_y(l)
    # 이 부분을 잘못생각했었는데 모든 연주를 쳐야할 필요는 없었다.
    # 연주를 하나라도 칠 수 있으면 결과값을 갱신
    if cnt < total_y:
        cnt = total_y
        ans = num

    elif cnt == total_y:
        if total_y != 0:
            ans = min(num, ans)

    if ''.join(l) == 'Y' * m:
        ans = min(num, ans)
        return

    if index == n:
        return

    for i in range(index, n):
        search(_or(l, guitars[i][1]), i + 1, num + 1)


search(['N' for _ in range(m)], 0, 0)
if ans == float('inf'):
    print(-1)
else:
    print(ans)

