import heapq

n = int(input())
gift_heap = []

for _ in range(n):
    data = list(map(int, input().split()))
    
    if data[0] == 0:
        if gift_heap:
            print(-heapq.heappop(gift_heap))
        else:
            print(-1)
    else:
        for value in data[1:]:
            heapq.heappush(gift_heap, -value)
