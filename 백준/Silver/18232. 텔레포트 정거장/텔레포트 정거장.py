from collections import deque

def bfs(graph, start, target, visited):
    
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        v, count = queue.popleft()
        
        if v == target:
            return count
        
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, count + 1))

        if v + 1 <= N and not visited[v + 1]:
            visited[v + 1] = True
            queue.append((v + 1, count + 1))
            
        if v - 1 >= 1 and not visited[v - 1]:
            visited[v - 1] = True
            queue.append((v - 1, count + 1))


N, M = map(int, input().split())
S, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False] * (N + 1)
result = bfs(graph, S, E, visited)
print(result)