# 다익스트라 알고리즘 이용
# 아이디어: 위치를 -1, +1, x2 하면서 거리 갱신
# 알고리즘 수행 후 최종 목적지의 거리 출력

import heapq

n, k = map(int, input().split())
MAX = 200001 # 배열 길이는 최대 입력의 2배
distance = [float('INF')] * MAX

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        if now + 1 < MAX and distance[now] + 1 < distance[now + 1]:
            cost = distance[now] + 1
            distance[now + 1] = cost
            heapq.heappush(queue, (cost, now + 1))
        if (now - 1) >= 0 and distance[now] + 1 < distance[now - 1]:
            cost = distance[now] + 1
            distance[now - 1] = cost
            heapq.heappush(queue, (cost, now - 1))
        if now * 2 < MAX and distance[now] < distance[now * 2]:
            cost = distance[now]
            distance[now * 2] = cost
            heapq.heappush(queue, (cost, now * 2))


dijkstra(n)
print(distance[k])