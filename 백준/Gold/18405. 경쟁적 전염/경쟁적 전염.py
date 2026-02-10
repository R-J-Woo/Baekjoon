from collections import deque

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 초기 바이러스의 위치 찾기
queue = deque()
# 작은 수부터 퍼지기 떄문에 작은 수부터 큐에 삽입
for num in range(1, K + 1):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                queue.append((i, j, graph[i][j]))

# S초 동안 바이러스 감염
for _ in range(S):
    # 이전 시간에 퍼진 바이러스의 수만큼만 진행
    # ex) 1초 때에 3개의 칸에만 바이러스가 퍼졌다면, 2초 때에는 그 퍼진 3개의 칸에 대해서만 작업
    count = len(queue)
    for _ in range(count):
        x, y, v = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy

            # 아직 바이러스가 퍼지지 않은 칸이라면
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = v
                queue.append((nx, ny, v))


print(graph[X-1][Y-1])