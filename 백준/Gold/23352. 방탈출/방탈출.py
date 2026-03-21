from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b, 0))
    visited[a][b] = True
    num1 = graph[a][b]
    num2 = 0
    move = 0 # 움직인 횟수

    while queue:
        x, y, count = queue.popleft()

        if count > move: # 이전 끝방보다 더 긴 경로
            move = count
            num2 = graph[x][y]
        elif count == move: # 이전 경로와 동일한 거리의 경로
            num2 = max(num2, graph[x][y])

        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return move, num1 + num2


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

result = 0
move = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            visited = [[False] * M for _ in range(N)]
            count, num = bfs(graph, i, j, visited)
            if count > move:
                move = count
                result = num
            elif count == move:
                result = max(result, num)


print(result)