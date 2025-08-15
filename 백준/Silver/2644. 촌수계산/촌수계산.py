# 아이디어: 너비 우선 탐색(BFS) 알고리즘 이용

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[0] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    if graph[x][0] == 0:
        graph[x][0] = y
    else:
        graph[x].append(y)

    if graph[y][0] == 0:
        graph[y][0] = x
    else:
        graph[y].append(x)


def bfs(graph, start, visited, result):
    queue = deque([start])
    visited[start] = True
    result[start] = 0

    # 1촌 관계의 사람들은 현재 촌수에서 +1을 해서 저장
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result[i] = result[v] + 1


result = [-1] * (n + 1)
visited = [False] * (n + 1)
bfs(graph, a, visited, result)
print(result[b])