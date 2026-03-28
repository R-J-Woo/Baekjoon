from collections import deque

def bfs(graph, a, b, visited):
    queue = deque()
    queue.append((a, b, 0)) # x좌표, y좌표, 이동한 격자의 개수
    visited[a][b] = True

    while queue:
        x, y, count = queue.popleft()
        booster = graph[x][y]

        if x == len(graph) - 1 and y == len(graph[0]) - 1:
            return count

        for i in range(1, booster + 1):

            # 아래쪽 이동
            if 0 <= x + i < len(graph) and not visited[x+i][y]:
                queue.append((x + i, y, count + 1))
                visited[x+i][y] = True

            # 오른쪽 이동
            if 0 <= y + i < len(graph[0])and not visited[x][y+i]:
                queue.append((x, y + i, count + 1))
                visited[x][y+i] = True
    

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

result = bfs(graph, 0, 0, visited)
print(result)