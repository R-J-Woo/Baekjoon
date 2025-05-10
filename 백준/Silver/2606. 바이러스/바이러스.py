from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

com_count = int(input())
connect_num = int(input())
visited = [False] * (com_count + 1)
graph = [[] for _ in range(com_count + 1)]

# 그래프 생성
for _ in range(connect_num):
    e1, e2 = map(int, input().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

bfs(graph, 1, visited)

count = 0
for visit in visited:
    if visit:
        count += 1

print(count - 1)