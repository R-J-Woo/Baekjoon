from collections import deque

def bfs(graph, start, target, visited):
    queue = deque()
    queue.append((start, 0)) # 현재 노드, 촌수
    visited[start] = True

    while queue:
        node, count = queue.popleft()
        if node == target:
            return count
        
        for v in graph[node]:
            if not visited[v]:
                queue.append((v, count + 1))
                visited[v] = True

    return -1


n = int(input())
a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
result = bfs(graph, a, b, visited)
print(result)