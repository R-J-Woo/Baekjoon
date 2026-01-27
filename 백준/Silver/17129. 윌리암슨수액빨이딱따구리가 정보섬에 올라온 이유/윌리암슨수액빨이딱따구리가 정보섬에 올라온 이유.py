import sys
from collections import deque

input = sys.stdin.readline

q = deque()
n, m = map(int, input().split())

graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 상, 하, 좌, 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start_x, start_y = 0, 0

# 시작점(2) 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            dx = x + d[i][0]
            dy = y + d[i][1]

            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] == 0 and graph[dx][dy] != 1:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append((dx, dy))

                    if graph[dx][dy] in (3, 4, 5):
                        return visited[dx][dy] - 1

    return -1

res = bfs(start_x, start_y)

if res != -1:
    print("TAK")
    print(res)
else:
    print("NIE")
