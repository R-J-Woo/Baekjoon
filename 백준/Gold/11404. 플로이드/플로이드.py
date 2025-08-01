# 아이디어: 플로이드 워셜 알고리즘 사용

import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b]) # 입력받은 노선 중에서 가장 작은 노션의 비용으로 채워넣음

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0,  end=" ")
        else:
            print(graph[i][j], end=" ")

    print()