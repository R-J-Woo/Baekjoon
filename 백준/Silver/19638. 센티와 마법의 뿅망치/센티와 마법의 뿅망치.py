import heapq

N, H, T = map(int, input().split())

big_guy = []
for _ in range(N):
    height = int(input())
    heapq.heappush(big_guy, -height)

count = 0
for i in range(T):
    max_height = -heapq.heappop(big_guy)

    if max_height < H or max_height == 1:
        heapq.heappush(big_guy, -max_height)
        break

    count += 1
    max_height = max_height // 2
    heapq.heappush(big_guy, -max_height)


if -min(big_guy) >= H:
    print("NO")
    print(-min(big_guy))
else:
    print("YES")
    print(count)