from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    size = 0
    while queue:
        x, y = queue.popleft()
        size += 1
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

    return size


N, M, K = map(int, input().split())
trash = [['.'] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    trash[a-1][b-1] = '#'

visited = [[False] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if trash[i][j] == '#':
            size = bfs(trash, i, j, visited)
            result = max(result, size)

print(result)