#제곱수의합 다시풀기
import sys
n = int(sys.stdin.readline().rstrip());

dp = [0]*(n+1);
print(n)
for i in range(1, n+1):
    dp[i] = i;             #1로 표현할 수 있는 최대값으로 초기화
i=0;
print(i,n)
for i in range( 1, n+1):
    for j in range( 1, i ):
        if( j*j > i ):break;
        dp[i] = min(dp[i], dp[i - j*j] +1 );

print(dp[n]);