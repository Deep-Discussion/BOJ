import collections

str = list(input())
str = collections.deque(str)
arr = []

while str:
    arr.append(''.join(str))
    str.popleft()

arr.sort()

for i in arr:
    print(i)