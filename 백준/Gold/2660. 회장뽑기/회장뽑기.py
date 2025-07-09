# 플로이드-워셜 알고리즘 사용

import sys
input = sys.stdin.readline

num = int(input())
INF = float('INF')
graph = [[INF] * (num + 1) for _ in range(num + 1)]

# 자기 자신은 0
for i in range(1, num + 1):
    graph[i][i] = 0

# 직접적인 친구 사이는 1
while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(1, num + 1):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

score, count = INF, 0
result = []
for i in range(1, num + 1):
    max_score = 0
    for j in range(1, num + 1):
        if graph[i][j] != INF and graph[i][j] > max_score:
            max_score = graph[i][j]

    if max_score == score:
        count += 1
        result.append(i)
    elif max_score < score:
        score = max_score
        count = 1
        result.clear()
        result.append(i)

print(score, len(result))
result.sort()
print(' '.join(str(num) for num in result))