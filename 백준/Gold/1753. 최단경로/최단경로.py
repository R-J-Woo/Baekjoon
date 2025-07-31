import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
distance = [float('INF')] * (v + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        # 이미 처리된 적이 있는 노드면 패스
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는게 기존보다 더 거리가 짧다면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(k)
for i in range(1, len(distance)):
    if distance[i] == float('INF'):
        print("INF")
    else:
        print(distance[i])