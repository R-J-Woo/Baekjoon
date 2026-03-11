from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
count = 0
for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        bfs(graph, i, visited)

print(count)