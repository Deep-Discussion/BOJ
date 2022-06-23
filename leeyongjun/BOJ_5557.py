import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split(' ')))
target = arr.pop()
ans = 0
_dp = [[0] * 21 for _ in range(n + 1)] #deps 마다 값을 저장


def dp(deps, num):
    global ans
    if num < 0 or num > 20:
        return
    if deps == n - 2:
        if num == target:
            ans += 1
        return
    dp(deps+1, num + arr[deps+1])
    dp(deps+1, num - arr[deps+1])


dp(0, arr[0])
print(ans)