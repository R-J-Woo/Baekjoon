# 아이디어: 도시에 bfs를 한번 돈 후에 거래소에 방문한 적이 있었다면 Yes, 아니면 No

from collections import deque
import sys
input = sys.stdin.readline

def bfs(city, visited, x, y, m, n):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    dx = [1, 0]
    dy = [0, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if city[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

n, m = map(int, input().split())  # n: 열, m: 행
city = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

bfs(city, visited, 0, 0, m, n)

if visited[m-1][n-1]:
    print("Yes")
else:
    print("No")
