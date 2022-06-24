n = int(input())
dp = [0] * 36

dp[0] = 1
dp[1] = 1
dp[2] = 2

# t(n) = t(0)*t(n-1) + t(1)*t(n-2) + ... + t(n-1)*t(0)
for i in range(3, n+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[n])
