# https://www.youtube.com/watch?v=kYoKLm8BZtI&t=442s 참고

n = int(input())

dp = [0 for _ in range(n+1)]
dp[0:3] = [1, 2, 7]# n = 1,2,3 인 경우

unusual_case = 0 #특이케이스 (가로로 나누어 지지 않는 경우)

# 점화식
# dp[i] = 2 * dp[i-1] + 3 * dp[i-2] + 2*(dp[i-3] ...... + dp[0])
# dp[i-1] * 2 -> 길이가 1 늘어 났을 때 1*2 과 1*1 두개로 배치하는 두가지 경우 발생
# dp[i-2] *3 -> 길이가 2 늘어 났을 때 (1*2 두개, 1*2, 1*1 두개, 1*1두개 1*2)
# 길이가 3인 단계부터 특이케이스가 2가지 경우씩 발생한다.

for i in range(3, n+1):
    unusual_case += dp[i-3]
    dp[i] = (2 * dp[i-1] + 3 * dp[i-2] + 2 * unusual_case) % 1000000007

print(dp[n])