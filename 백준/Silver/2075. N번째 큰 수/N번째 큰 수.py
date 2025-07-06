import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            # 현재 수가 최소 힙의 루트보다 크면 교체
            if num > heap[0]:
                heapq.heappushpop(heap, num)

print(heap[0])