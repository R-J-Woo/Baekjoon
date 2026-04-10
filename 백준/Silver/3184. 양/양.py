from collections import deque

def bfs(graph, x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    sheep = 0
    wolf = 0

    if graph[x][y] == 'o':
        sheep += 1
    elif graph[x][y] == 'v':
        wolf += 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

                if graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1

    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf
    

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
total_sheep = 0
total_wolf = 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph[i][j] != '#':
            s, w = bfs(graph, i, j, visited)
            total_sheep += s
            total_wolf += w

print(total_sheep, total_wolf)