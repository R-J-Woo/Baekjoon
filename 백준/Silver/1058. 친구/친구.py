import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)

graph = [[INF] * n for _ in range(n)]

# 친구 정보 입력받고 그래프 초기화
# N x N 복잡도
for i in range(n):
    is_friends = input()
    for j in range(len(is_friends)):
        if is_friends[j] == 'Y':
            graph[i][j] = 1

# 플로이드 워셜 알고리즘 수행
# N x N x N 복잡도
for k in range(n):
    for a in range(n):
        for b in range(n):
            if (graph[a][k] + graph[k][b]) < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b] # graph[a][b]에 1을 넣으면 몇번 건너서 친구인지 파악 안됨 -> graph[a][k] + graph[k][b]으로 몇다리 건너 친구인지 확인 가능

max_count = 0
for a in range(n):
    temp = 0
    for b in range(n):
        if a != b and graph[a][b] <= 2:
            temp += 1
    max_count = max(max_count, temp)

print(max_count)