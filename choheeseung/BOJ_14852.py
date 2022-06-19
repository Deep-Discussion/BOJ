n = int(input())
dp = [0 for _ in range(n+2)]

dp[0] = 1
dp[1] = 2
dp[2] = 7

if n <= 2:
    print(dp[n])
    quit()

for i in range(3, n+1):
    dp[i] = (dp[i-1] * 3 + dp[i-2] - dp[i-3]) % 1000000007

print(dp[n] % 1000000007)
