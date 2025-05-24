import heapq
import sys
input = sys.stdin.readline

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


N, M, K, X = map(int, input().split())

INF = int(1e9)
visited = [False] * (N + 1)
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))

dijkstra(X)

count = 0
for i in range(1, N + 1):
    if distance[i] == K:
        count += 1
        print(i)

if count == 0:
    print(-1)