from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append((start, 0)) # 현재 학번, 친구 건너뛴 수
    visited[start] = True
    count = 0

    while queue:
        node, move = queue.popleft()
        
        if move > 1:
            continue
        
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                count += 1
                queue.append((v, move + 1))

    return count


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = bfs(graph, 1, visited)

print(result)