import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
heap = []

for _ in range(N):
    current_row_matrix = list(map(int, input().split()))
    if heap:
        for number in current_row_matrix:

            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)

    else:
        for number in current_row_matrix:
            heapq.heappush(heap, number)

print(heap[0])
