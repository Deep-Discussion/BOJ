# 용사가 n번 공격하면 n-1번 공격당함.
import sys

n, h_atk = map(int, sys.stdin.readline().split())
# max_hp를 구해야 함
max_hp, cur_hp, damage = 0, 0, 0

for i in range(n):
    t, a, h = map(int, sys.stdin.readline().split())
    if t == 1:  # 안에 몬스터가 있음
        temp = h % h_atk
        if temp == 0:
            damage = -(a * (h // h_atk - 1))
        else:
            damage = -(a * (h // h_atk))
    else:  # 포션 방
        h_atk += a
        damage = h
    cur_hp += damage
    if cur_hp > 0:
        cur_hp = 0
    max_hp = max(max_hp, abs(cur_hp))

print(max_hp + 1)
