from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            # 같은 색의 동그라미가 이어져 있으면 실패
            if visited[i] == visited[v]:
                return False

            if visited[i] == 0:
                queue.append(i)
                if visited[v] == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1

    return True     


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 0:
            flag = bfs(graph, i, visited)
            if not flag:
                break

    if flag:
        print("possible")
    else:
        print("impossible")