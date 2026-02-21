from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    height = graph[a][b]
    flag = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] > height:
                    flag = False

                if graph[nx][ny] == height and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return flag


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            is_peak = bfs(graph, i, j, visited)
            if is_peak:
                count += 1

print(count)