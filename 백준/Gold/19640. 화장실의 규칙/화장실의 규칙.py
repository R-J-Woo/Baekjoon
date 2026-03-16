import heapq
from collections import deque

N, M, K = map(int, input().split())

lines = [deque() for _ in range(M)]

for i in range(N):
    D, H = map(int, input().split())
    line = i % M
    lines[line].append((D, H, i))

heap = []

for i in range(M):
    if lines[i]:
        D, H, idx = lines[i].popleft()
        heapq.heappush(heap, (-D, -H, i, idx))

count = 0

while heap:
    D, H, line, idx = heapq.heappop(heap)

    if idx == K:
        print(count)
        break

    count += 1

    if lines[line]:
        D, H, idx = lines[line].popleft()
        heapq.heappush(heap, (-D, -H, line, idx))