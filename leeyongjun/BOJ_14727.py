n, t = map(int, input().split(' '))
data = []
for _ in range(n):
    data.append(list(map(int, input().split(' '))))

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, t+1):
        if j >= data[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-data[i-1][0]] + data[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])
