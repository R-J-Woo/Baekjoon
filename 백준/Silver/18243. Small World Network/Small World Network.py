# 아이디어: 플로이드 워셜 알고리즘 사용

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[float('INF')] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

flag = False
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] > 6:
            flag = True
            break

    if flag == True:
        break


if flag == True:
    print("Big World!")
else:
    print("Small World!")