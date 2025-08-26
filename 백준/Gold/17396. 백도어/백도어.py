# 아이디어: 다익스트라 알고리즘 이용

import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
can_visit = list(map(int, input().strip().split()))

graph = [[] for _ in range(n)]
distance = [float('INF')] * n
for _ in range(m):
    a, b, t = map(int, input().split())
    # 양방향으로 연결
    graph[a].append((b, t))
    graph[b].append((a, t))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        # 현재 가장 짧은 거리의 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)
        
        # 이미 방문한 적이 있으면 패스
        if distance[now] < dist:
            continue

        # 시야에 보이는 곳이면 패스
        if can_visit[now] == 1 and now != (n - 1):
            continue

        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는게, 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(0)
if distance[-1] == float('INF'):
    print(-1)
else:
    print(distance[-1])