from collections import deque

def bfs(graph, a, b, visited, jump):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    row = len(graph)
    col = len(graph[0])

    while queue:
        x, y = queue.popleft()
        
        if x == (row - 1) and y == (col - 1):
            return True
        
        for dx in range(-jump, jump + 1):
            for dy in  range(-jump, jump + 1):
                if abs(dx) + abs(dy) <= jump:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    return False


N = int(input())
M = int(input())
road = []
for _ in range(N):
    road.append(list(map(int, input().split())))
X = int(input())

visited = [[False] * M for _ in range(N)]
flag = bfs(road, 0, 0, visited, X)

if flag:
    print("ALIVE")
else:
    print("DEAD")