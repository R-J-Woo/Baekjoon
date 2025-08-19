from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 노드 오름차순 정렬
for node in graph:
    node.sort()


def bfs(graph, start, visited):
    count = 1
    visited[start] = count
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for v in graph[node]:
            if visited[v] == 0:
                count += 1
                visited[v] = count # 방문 순서 저장
                queue.append(v)


visited = [0] * (n + 1)
bfs(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])