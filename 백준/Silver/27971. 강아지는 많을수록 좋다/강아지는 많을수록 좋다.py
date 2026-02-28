from collections import deque

N, M, A, B = map(int, input().split())

# 닫힌 구간에 방문하지 못하도록 미리 visited를 True로 설정
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        visited[i] = True

queue = deque()
queue.append((0, 0))
visited[0] = True

flag = False
result = 100000
while queue:
    dog, move = queue.popleft()

    if dog == N:
        flag = True
        result = min(result, move)

    for plus_dog in [A, B]:
        next = dog + plus_dog
        if next <= N and not visited[next]:
            visited[next] = True
            queue.append((next, move + 1))

if flag:
    print(result)
else:
    print(-1)