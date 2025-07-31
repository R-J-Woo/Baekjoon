# 아이디어: 다익스트라 알고리즘 사용

import heapq
import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [float('INF')] * (n + 1)

for _ in range(m):
    A, B, C = map(int, input().split())
    graph[A].append((B, C)) # A -> B로 가는 길에 소 C 마리
    graph[B].append((A, C)) # B -> A로 가는 길에 소 C 마리

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)

        # 이미 방문했던 곳이라면 패스
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는 경우가 더 나은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(1)

print(distance[n])