from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, n + 1):
    if visited[i] == False:
        bfs(graph, i, visited)
        count += 1

print(count)