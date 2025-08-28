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
        if visited[i] == True:
            cycle_flag = True
            return
        else:
            dfs(graph, i, visited)

    visited[start] = False

visited = [False] * (n + 1)    
dfs(graph, 1, visited)
if cycle_flag == True:
    print("CYCLE")
else:
    print("NO CYCLE")