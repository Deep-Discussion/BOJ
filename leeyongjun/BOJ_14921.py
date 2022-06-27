import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split(' ')))

# N <= 100,000 완탐 O(N^2) -> O(n)처리 해야될듯..

left, right = 0, n - 1
ans = arr[left] + arr[right]

while left < right:
    mix_value = arr[left] + arr[right]
    if abs(ans) > abs(mix_value):
        ans = mix_value

    if mix_value < 0:
        left += 1
    else:
        right -= 1

print(ans)