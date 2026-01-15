import sys
input = sys.stdin.readline


N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = INF
building = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        total = 0
        for k in range(1, N + 1):
            total += min(graph[i][k], graph[j][k])

        if total * 2 < result:
            building.append(i)
            building.append(j)
            result = total * 2

building.sort()
for b in building:
    print(b, end=" ")
    
print(result)