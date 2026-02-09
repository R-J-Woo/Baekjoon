from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == graph[a][b] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count


col, row = map(int, input().split())

graph = []
for _ in range(row):
    graph.append(list(input()))

visited = [[False] * col for _ in range(row)]
white = 0
blue = 0
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            count = bfs(graph, i, j, visited)
            if graph[i][j] == 'W':
                white += count ** 2
            else:
                blue += count ** 2

print(white, blue)