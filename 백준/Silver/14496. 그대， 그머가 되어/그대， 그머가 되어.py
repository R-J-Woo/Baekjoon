from collections import deque

def bfs(graph, start, target, visited):
    queue = deque()
    queue.append((start, 0)) # 위치, 움직인 횟수
    visited[start] = True

    result = -1
    while queue:
        num, count = queue.popleft()

        if num == target:
            return count
        
        for v in graph[num]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, count + 1))

    return result


a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)
result = bfs(graph, a, b, visited)

print(result)