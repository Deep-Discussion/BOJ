import sys

n, atk = map(int, input().split(' '))

room_info = []

for _ in range(n):
    room_info.append(list(map(int, sys.stdin.readline().split(' '))))

max_hp, cur_hp, _min = 0, 0, 0

# 추가 테스트 케이스에서 코드의 문제점을 발견
# 8 3
# 1 1 31
# 1 1 31
# 1 1 31
# 1 1 31
# 1 1 31
# 1 1 31
# 2 3 70
# 1 3 100
# 회복량이 그동안 쌓아온 누적 데미지 보다 높아질 때 max_hp 값으로 변동 해주었는데 누적되는 데미지보다 높은 량이 max_hp 로 지정 되어야 했다.
for room in room_info:
    t, a, h = room
    if t == 1:
        q, r = divmod(h, atk)
        if r != 0:
            q += 1
        cur_hp -= a * (q-1)
        _min = max(cur_hp * -1, _min)
    else:
        cur_hp, atk = cur_hp + h, atk + a
        if cur_hp > max_hp:
            cur_hp = max_hp

print(_min + 1)