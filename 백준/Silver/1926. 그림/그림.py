from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    width = 0
    while queue:
        x, y = queue.popleft()
        width += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return width

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
paint = 0
width = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            paint += 1
            pw = bfs(graph, i, j, visited)
            width = max(width, pw)

print(paint)
print(width)