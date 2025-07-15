# 아이디어: 너비 우선 탐색으로 다음 먹을 수 있는 곳 중 가장 짧은 거리를 탐색
# 더 이상 먹을 수 있는 물고기가 없으면 종료

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 아기 상어 위치, 크기, 먹은 횟수
shark_size = 2
eat_count = 0
time = 0

# 아기 상어 위치 찾기
shark_x, shark_y = 0, 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            shark_x = i
            shark_y = j
            maps[i][j] = 0

# BFS로 먹을 수 있는 물고기 탐색
def bfs(x, y):
    visited = [[False]*n for _ in range(n)]
    dist_list = []  # (거리, x, y)
    queue = deque()
    queue.append((x, y, 0))  # x, y, 거리
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy, dist = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 이동 가능한 조건: 물고기 크기 <= 상어 크기
                if maps[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    # 먹을 수 있는 경우: 0 < 크기 < 상어 크기
                    if 0 < maps[nx][ny] < shark_size:
                        dist_list.append((dist+1, nx, ny))
                    queue.append((nx, ny, dist+1))

    # 먹을 수 있는 물고기 없으면
    if not dist_list:
        return None
    # 우선순위: 거리, 위쪽, 왼쪽
    dist_list.sort()
    return dist_list[0]  # 가장 우선순위 높은 물고기 반환


while True:
    result = bfs(shark_x, shark_y)
    if result is None:
        break  # 먹을 수 있는 물고기 없음

    dist, nx, ny = result
    time += dist
    eat_count += 1
    maps[nx][ny] = 0  # 물고기 먹음
    shark_x, shark_y = nx, ny  # 상어 위치 이동

    # 상어 크기 증가 조건
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(time)