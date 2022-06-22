import sys

n, k = map(int, input().split())

Lvs = [int(input()) for _ in range(n)]

Lvs.sort()

left = Lvs[0]
right = Lvs[-1] + k
ans = 0

# 이분탐색을 이용한 구현
# 정렬된 리스트 값에서 `목표레벨`을 기준으로 각 레벨마다 필요한 레벨량과 주어진 올릴 수 있는 레벨 총합 K 를 바탕으로 탐색
# sum(목표레벨 - 현재레벨)의 값과 K 값을 비교  K값보다 작으면 right = mid + 1 작거나 같으면 left = mid - 1
while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for Lv in Lvs:
        if mid > Lv:
            cnt += (mid - Lv)

    if cnt > k:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)