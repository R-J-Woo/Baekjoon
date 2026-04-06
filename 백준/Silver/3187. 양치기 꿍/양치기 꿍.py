from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    wolf = []
    sheep = []

    while queue:
        x, y = queue.popleft()

        if graph[x][y] == 'v':
            wolf.append((x, y))
        elif graph[x][y] == 'k':
            sheep.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] != '#' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    if len(wolf) < len(sheep):
        for x, y in wolf:
            graph[x][y] = '.'
    else:
        for x, y in sheep:
            graph[x][y] = '.'


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] != "#":
            bfs(graph, i, j, visited)

wolf, sheep = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'v':
            wolf += 1
        elif graph[i][j] == 'k':
            sheep += 1

print(sheep, wolf)