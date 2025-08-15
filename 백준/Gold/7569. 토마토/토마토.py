# 아이디어: 너비 우선 탐색(BFS) 알고리즘 이용

from collections import deque
import sys
input = sys.stdin.readline

# 3차원 리스트 입력 받기
m, n, h = map(int, input().split())
box = []
for _ in range(h):
    layer = []
    for _ in range(n):
        layer.append(list(map(int, input().split())))

    box.append(layer)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 1]

def bfs():
    queue = deque()
    result = [[[10001] * m for _ in range(n)] for _ in range(h)]

    # 처음부터 익어있는 토마토 찾기
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if box[k][i][j] == 1:
                    result[k][i][j] = 0
                    queue.append((k, i, j))

    while queue:
        z, x, y = queue.popleft()
        
        # 앞뒤좌우
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m\
                and box[z][nx][ny] == 0 and result[z][nx][ny] == 10001:
                box[z][nx][ny] = 1
                queue.append((z, nx, ny))
                # 이전 일수에서 1일 추가
                result[z][nx][ny] = result[z][x][y] + 1
        # 상하
        for i in range(2):
            nz = z + dz[i]
            if 0 <= nz < h and box[nz][x][y] == 0 and result[nz][x][y] == 10001:
                box[nz][x][y] = 1
                queue.append((nz, x, y))
                # 이전 일수에서 1일 추가
                result[nz][x][y] = result[z][x][y] + 1

    return result


result = bfs()

# 익지 않은 토마토가 있는지 찾기
for i in range(n):
    for j in range(m):
        for k in range(h):
            if box[k][i][j] == 0:
                print(-1)
                exit()

day = 0
for i in range(n):
    for j in range(m):
        for k in range(h):
            if result[k][i][j] != 10001:
                day = max(day, result[k][i][j])

print(day)