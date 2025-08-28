# 아이디어: 플로이드 워셜 알고리즘 이용

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[float('INF')] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# 자기 자신으로의 길은 길이가 0이다
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이도 워셜 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 각 지역을 시작으로 얻을 수 있는 아이템 최대 개수 탐색
result = 0
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m: # 수색 범위 이내라면 아이템 추가
            total += item[j]

    result = max(result, total)

print(result)