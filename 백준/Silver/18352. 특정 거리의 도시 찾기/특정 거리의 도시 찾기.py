from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 0  # 시작 노드 거리 0

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if visited[nxt] == -1:  # 방문 안 한 경우
                visited[nxt] = visited[node] + 1
                queue.append(nxt)


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [-1] * (N + 1)

bfs(graph, X, visited)

result = []
for i in range(1, N + 1):
    if visited[i] == K:
        result.append(i)

if not result:
    print(-1)
else:
    for r in result:
        print(r)