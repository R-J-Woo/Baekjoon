from collections import deque

N, a, b = map(int, input().split())

visited = [False] * (N + 1)
queue = deque()
queue.append((N, 0))  # (현재 앞에 남은 인원, 시간)
visited[N] = True

while queue:
    x, time = queue.popleft()

    if x == 0:
        print(time)
        break

    # 1번 행동
    if x - 1 >= 0 and not visited[x - 1]:
        visited[x - 1] = True
        queue.append((x - 1, time + 1))

    # a번 행동
    if x - a - 1 >= 0 and not visited[x - a - 1]:
        visited[x - a - 1] = True
        queue.append((x - a - 1, time + 1))

    # b번 행동
    if x - b - 1 >= 0 and not visited[x - b - 1]:
        visited[x - b - 1] = True
        queue.append((x - b - 1, time + 1))