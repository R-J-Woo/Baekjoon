import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 현재 위치 방문 처리
    visited[y][x] = True
    
    # 8방향 탐색 (상하좌우 + 대각선)
    for dx, dy in [(-1, -1), (0, -1), (1, -1),
                   (-1,  0),          (1,  0),
                   (-1,  1), (0,  1), (1,  1)]:
        nx = x + dx
        ny = y + dy
        # 지도 범위 안에 있고, 땅(1)이면서 아직 방문 안했으면
        if 0 <= nx < w and 0 <= ny < h:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    count = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1
    print(count)
