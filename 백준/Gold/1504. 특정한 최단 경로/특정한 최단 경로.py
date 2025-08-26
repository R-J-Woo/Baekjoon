# 아이디어: 다익스트라 알고리즘 이용
# 다익스트라를 3번 실행
# 1 -> 모든 정점 / v1 -> 모든 정점 / v2 -> 모든 정점
# 두 가지 경로를 구해서 최단 거리 확인 = 1 -> v1 -> v2 -> N / 1 -> v2 -> v1 -> N

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = [(0, start)]
    
    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(heap, (cost, nxt))
    return distance

# 입력
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 무방향 그래프

v1, v2 = map(int, input().split())

# 다익스트라 실행
dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# 두 가지 경로 계산
path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

answer = min(path1, path2)
if answer < INF:
    print(answer)
else:
    print(-1)
