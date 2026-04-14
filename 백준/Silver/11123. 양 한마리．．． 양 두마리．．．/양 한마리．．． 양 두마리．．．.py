from collections import deque

def bfs(graph, x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    result = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(grid, i, j, visited)
                result += 1

    print(result)