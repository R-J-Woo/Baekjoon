# 아이디어: visited로 방문했는지를 판단하고 몇 번째에 방문했는지 저장한다

import heapq
import sys
sys.setrecursionlimit(10**6) # 재귀함수 사용할 때는 런타임 에러 방지
input = sys.stdin.readline


def dfs(graph, start, visited):
    # 몇 번째 방문인지 저장
    global count
    count += 1
    visited[start] = count

    for v in graph[start]:
        # 방문한 적이 없다면 방문
        if visited[v] == 0:
            dfs(graph, v, visited)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순으로 정렬
for i in range(1, n + 1):
    graph[i].sort()

visited = [0] * (n + 1)
count = 0
dfs(graph, r, visited)

for v in visited[1:]:
    print(v)