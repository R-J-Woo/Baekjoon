from collections import deque

n, m = map(int, input().split())

# 원본 영상 (N행 M열, RGB 3개씩)
image = []
for _ in range(n):
    row = list(map(int, input().split()))
    pixels = [row[i:i+3] for i in range(0, len(row), 3)]
    image.append(pixels)

T = int(input())

# 이진화 영상 생성
binary = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        R, G, B = image[i][j]
        gray = (R + G + B) // 3
        if gray >= T:
            binary[i][j] = 255
        else:
            binary[i][j] = 0

# 4방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if binary[nx][ny] == 255 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 연결된 영역 개수 세기
visited = [[False]*m for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if binary[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
