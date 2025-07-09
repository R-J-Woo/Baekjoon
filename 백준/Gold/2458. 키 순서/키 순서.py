# 플로이드-워셜 알고리즘 사용
# 각 학생에 대해 작은 학생 수 + 큰 학생 수가 n - 1인지 확인

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 행열 중 4가 들어가 있는 것이 INF가 아니면 체크
answer = 0
for i in range(1, n + 1):
    known = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            known += 1
    if known == n:
        answer += 1

print(answer)