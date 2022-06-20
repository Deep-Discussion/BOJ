import heapq
import sys
from queue import PriorityQueue

n = int(input())
q = []


#Max-heap 구현시 메모리 초과
# for i in range(n):
#     for j in range(n):
#         q.put((1/board[i][j], board[i][j]))
#
# for _ in range(n-1):
#     q.get()
val = 0
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split(' ')))
    if not q:
        for num in nums:
            heapq.heappush(q, num)

    else:
        for num in nums:
            #길이가 N인 우선순위큐를 유지하고 최소값보다 큰 값만 계속 넣어준다.
            if q[0] < num:
                heapq.heappush(q, num)
                heapq.heappop(q)

print(q[0])
