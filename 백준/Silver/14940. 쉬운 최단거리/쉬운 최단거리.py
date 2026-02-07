from collections import deque

n, m = map(int, input().split())
graph = []
a, b = 0, 0
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

    if 2 in row:
        j = row.index(2)
        a, b = i, j


result = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result[i][j] = 0

queue = deque()
queue.append((a, b, 0))
result[a][b] = 0

while queue:
    x, y, dist = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # 갈 수 있는 땅 & 이미 간적 없는 땅
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and result[nx][ny] == -1:
            result[nx][ny] = dist + 1
            queue.append((nx, ny, dist + 1))

for row in result:
    print(' '.join(map(str, row)))