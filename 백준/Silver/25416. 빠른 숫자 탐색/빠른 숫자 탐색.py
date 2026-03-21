from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b, 0))
    visited[a][b] = True

    while queue:
        x, y, count = queue.popleft()

        if graph[x][y] == 1:
            return count
        
        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and graph[nx][ny] != -1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return -1


board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

visited = [[False] * 5 for _ in range(5)]
result = bfs(board, r, c, visited)

print(result)