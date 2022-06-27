import sys

n = int(input())
dist = list(map(int, sys.stdin.readline().split(' ')))
prices = list(map(int, sys.stdin.readline().split(' ')))

price = prices[0]
ans = price * dist[0]

for i in range(1, len(dist)):
    price = min(price, prices[i])
    ans += dist[i] * price

print(ans)

