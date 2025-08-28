# 아이디어: 깊이 우선 탐색(DFS) 알고리즘 이용
# 깊이 우선 탐색을 돌면서 visited를 이용해서 방문한 적 있는 노드에 다시 방문했음을 판단

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    m = int(input())
    c = list(map(int, input().split()))
    graph[i] = c

cycle_flag = False
def dfs(graph, start, visited):
    global cycle_flag
    visited[start] = True
    for i in graph[start]:
        if visited[i] == True: # 이미 방문한 적이 있는 노드라면 CYCLE
            cycle_flag = True
            return
        else:
            dfs(graph, i, visited)

    visited[start] = False # 다시 돌아갈 때 방문한 적 없는 상태로 복구

visited = [False] * (n + 1)    
dfs(graph, 1, visited)
if cycle_flag == True:
    print("CYCLE")
else:
    print("NO CYCLE")