import sys

h, w = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

left, right = 0, w - 1
left_max, right_max = heights[left], heights[right]

ans = 0

# two pointer
# brute force 로 풀어봤는데 참고자료에서 two pointer 풀이법이 있어서 참고하였다
while left < right:
    left_max = max(left_max, heights[left])
    right_max = max(right_max, heights[right])

    if left_max >= right_max:
        ans += right_max - heights[right]
        right -= 1
    if left_max < right_max:
        ans += left_max - heights[left]
        left += 1

print(ans)
