# 아이디어: 너비 우선 탐색(BFS) 알고리즘 이용

from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            paper[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    count = 0

    # 상하좌우 확인
    while queue:
        # 영역의 개수 1 추가
        count += 1
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return count


visited = [[False] * n for _ in range(m)]
result = []
area = 0
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0 and not visited[i][j]:
            area += 1
            count = bfs(paper, i, j, visited)
            result.append(count)

result.sort()
print(area)
print(' '.join(str(num) for num in result))