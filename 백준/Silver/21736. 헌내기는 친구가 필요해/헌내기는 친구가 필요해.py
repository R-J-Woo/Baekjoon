from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

# 현재 도연이의 위치 찾기
a, b = 0, 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            a, b = i, j

queue = deque()
queue.append((a, b))
visited[a][b] = True

count = 0
while queue:
    x, y = queue.popleft()

    if campus[x][y] == 'P':
        count += 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and campus[nx][ny] in ('O', 'P'):
            visited[nx][ny] = True
            queue.append((nx, ny))


if count == 0:
    print("TT")
else:
    print(count)