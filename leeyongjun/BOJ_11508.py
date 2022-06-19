#편의점 2+1 중에 가장 가성비 좋게 고르는 문제
n = int(input())
values = []

for _ in range(n):
    values.append(int(input()))

values.sort(reverse=True)
ans = 0
for i in range(n):
    if i % 3 == 2:
        continue
    ans += values[i]

print(ans)