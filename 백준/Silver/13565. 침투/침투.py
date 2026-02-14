from collections import deque

def bfs(graph, a, b):
    graph[a][b] = 2
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

M, N = map(int, input().split())

graph = []
for _ in range(M):
    graph.append(list(map(int, input())))

for i in range(N):
    if graph[0][i] == 0:
        bfs(graph, 0, i)

flag = False
for i in range(N):
    if graph[M - 1][i] == 2:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")