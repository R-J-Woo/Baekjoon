# 아이디어: 방향없는 그래프로 DFS 진행
# 아직 방문하지 않은 노드를 방문할 시, 그 현재 노드를 이동할 노드의 부모라고 지정

import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 초과로 런타임 에러 발생, 재귀 한도 늘리기
input = sys.stdin.readline

def dfs(graph, v, visited, parents):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            parents[i] = v
            dfs(graph, i, visited, parents)

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
parents = [0] * (n + 1)
dfs(graph, 1, visited, parents)

for i in range(2, n + 1):
    print(parents[i])