# 아이디어: 게임 구역을 bfs로 탐색
# 승리지점에 방문한 적이 있으면 HaruHaru, 아니면 Hing
from collections import deque
import sys
input = sys.stdin.readline

def bfs(area, visited):
    visited[0][0] = True
    queue = deque()
    queue.append((0, 0))
    dx = [0, 1]
    dy = [1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i] * area[x][y]
            ny = y + dy[i] * area[x][y]

            # 구역을 벗어나면 패스
            if nx < 0 or nx >= len(area) or ny < 0 or ny >= len(area):
                continue

            # 이미 방문한 적이 있으면 패스
            if visited[nx][ny] == True:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True



n = int(input())
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

bfs(area, visited)

if visited[n-1][n-1] == True:
    print("HaruHaru")
else:
    print("Hing")