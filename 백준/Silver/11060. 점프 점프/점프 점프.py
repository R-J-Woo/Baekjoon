from collections import deque

N = int(input())
A = list(map(int, input().split()))

queue = deque()
queue.append((0, 0))

visited = [False] * N
visited[0] = True

result = -1
while queue:
    idx, count = queue.popleft()

    if idx + 1 == N:
        result = count
        break

    for move in range(1, A[idx] + 1):
        nxt = idx + move
        if nxt < N and not visited[nxt]:
            queue.append((nxt, count + 1))
            visited[nxt] = True

print(result)