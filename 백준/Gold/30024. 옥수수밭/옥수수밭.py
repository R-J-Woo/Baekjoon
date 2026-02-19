import heapq

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

visited = [[False] * M for _ in range(N)]
queue = []

# 가장 자리 옥수수를 우선순위 큐에 넣음
for i in range(N):
    heapq.heappush(queue, (-graph[i][0], i, 0))
    heapq.heappush(queue, (-graph[i][M - 1], i, M - 1))

for j in range(1, M - 1):
    heapq.heappush(queue, (-graph[0][j], 0, j))
    heapq.heappush(queue, (-graph[N - 1][j], N - 1, j))

count = 0
result = []

while queue and count < K:
    corn, x, y = heapq.heappop(queue)

    if visited[x][y]:
        continue

    visited[x][y] = True
    result.append((x, y))
    count += 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            heapq.heappush(queue, (-graph[nx][ny], nx, ny))

for x, y in result:
    print(x + 1, y + 1)