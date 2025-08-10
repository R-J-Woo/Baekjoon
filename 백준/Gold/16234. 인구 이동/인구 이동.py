# 아이디어: bfs 너비 우선 탐색 이용
# 각 연합을 구하고, 연합 별로 평균을 따로 계산해야 한다

from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]
    total = area[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(area[cx][cy] - area[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total += area[nx][ny]
    return union, total

count = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total = bfs(i, j, visited)
                if len(union) > 1:  # 연합이 형성되면 인구 이동
                    moved = True
                    avg = total // len(union)
                    for ux, uy in union:
                        area[ux][uy] = avg

    if not moved:  # 더 이상 인구 이동 없음
        break
    count += 1

print(count)
