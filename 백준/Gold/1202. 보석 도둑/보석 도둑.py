import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
mv_list = []
c_list = []
for _ in range(n): # O(N)
    heapq.heappush(mv_list, tuple(map(int, input().split())))

for _ in range(k): # O(N)
    heapq.heappush(c_list, int(input()))

queue = []
result = 0
while c_list:
    c = heapq.heappop(c_list)
    while mv_list and mv_list[0][0] <= c:
        weight, value = heapq.heappop(mv_list)
        heapq.heappush(queue, -value)

    if queue:
        result -= heapq.heappop(queue)

print(result)