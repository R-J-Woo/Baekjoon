import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 그래프
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블
distance = [float('INF')] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

# 다익스트라 함수
def dijkstra(start):
    queue = []
    # 시작노드에 대해서는 거리를 0으로 설정하고 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
print(distance[end])