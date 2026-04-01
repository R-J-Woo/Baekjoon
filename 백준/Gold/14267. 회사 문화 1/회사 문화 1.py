from collections import deque

n, m = map(int, input().split())
upper = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

root = 0
for i in range(n):
    if upper[i] == -1:
        root = i + 1
    else:
        graph[upper[i]].append(i + 1)

# 칭찬 누적만 먼저 기록
result = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    result[i] += w

# 한 번만 BFS로 전파
queue = deque([root])

while queue:
    node = queue.popleft()
    for child in graph[node]:
        result[child] += result[node]
        queue.append(child)

print(*result[1:])