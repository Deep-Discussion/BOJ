# import sys
#
# n = int(input())
# arr = list(map(int, sys.stdin.readline().split(' ')))
# target = arr.pop()
# ans = 0
# _dp = [[0] * 21 for _ in range(n + 1)] #deps 마다 값을 저장
#
#
# def dp(deps, num):
#     global ans
#     if num < 0 or num > 20:
#         return
#     if deps == n - 2:
#         if num == target:
#             ans += 1
#         return
#     dp(deps+1, num + arr[deps+1])
#     dp(deps+1, num - arr[deps+1])
#
#
# dp(0, arr[0])
# print(ans)

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 21 for _ in range(N)]
# dp[idx번째][현재까지의 수] = 가능한 경우의 수
dp[0][arr[0]] += 1
for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if j + arr[i] <= 20: dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0: dp[i][j - arr[i]] += dp[i - 1][j]
print(dp[N - 2][arr[N - 1]])