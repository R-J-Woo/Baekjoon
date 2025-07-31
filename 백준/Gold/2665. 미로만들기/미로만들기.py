# 아이디어: 다익스트라
# 각 좌표를 노드라고 생각
# 흰 방은 가중치 0, 검은 방은 가중치 1
# 최소 벽 부수는 횟수를 기준으로 다익스트라

import heapq
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

# visited[x][y] = (x, y)까지 오는데 부순 벽 개수
visited = [[float('inf')] * n for _ in range(n)]
visited[0][0] = 0

# 우선순위 큐: (벽 부순 횟수, x, y)
heap = [(0, 0, 0)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while heap:
    cost, x, y = heapq.heappop(heap)

    if x == n - 1 and y == n - 1:
        print(cost)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            # 다음 방이 흰 방이면 cost 그대로
            # 검은 방이면 cost + 1
            new_cost = cost + (1 if graph[nx][ny] == 0 else 0)
            if visited[nx][ny] > new_cost:
                visited[nx][ny] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny))