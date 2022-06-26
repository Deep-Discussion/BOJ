# n = int(input())
#
# result = 0
# a = [[] for _ in range(n+1)]
# for _ in range(n):
#     point, color = map(int, input().split(' '))
#     a[color].append(point)
#
#
# def dis(arr):
#     ans = 0
#
#     for i in range(0, len(arr)):
#         if i == 0:
#             ans += arr[1] - arr[0]
#         elif i == len(arr)-1:
#             ans += arr[i] - arr[i-1]
#         else:
#             ans += min(arr[i] - arr[i-1], arr[i+1]-arr[i])
#     return ans
#
#
# for i in range(1, n):
#     a[i].sort()
#     result += dis(a[i])
#
# print(result)

import sys
n = int(sys.stdin.readline())

a = [[] for _ in range(n + 1)]

for i in range(n):
    coord, color = map(int, sys.stdin.readline().split())
    a[color].append(coord)

def toLeft(color, i):
    if i == 0:
        return 1000000
    return a[color][i] - a[color][i - 1]

def toRight(color, i):
    if i + 1 == len(a[color]):
        return 1000000
    return a[color][i + 1] - a[color][i]


ans = 0
for color in range(1, n + 1):
    a[color].sort()
    for i in range(len(a[color])):
        ans += min(toLeft(color, i), toRight(color, i))

print(ans)
