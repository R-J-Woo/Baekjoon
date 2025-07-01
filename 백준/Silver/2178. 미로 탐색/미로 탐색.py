# 아이디어: maps를 이용, 그 해당 노드에 이전에 방문했던 길이보다 현재 이 길로 방문한 경우가 더 짧을 경우 갱신
# graph는 길을 표시, visited는 직전에 방문한 곳은 다시 가지 않기 위해 사용

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, x, y, maps, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    count = 0
    while queue:
        count += 1
        dx, dy = queue.popleft()
        if dx + 1 < len(graph) and graph[dx+1][dy] == 1 and visited[dx+1][dy] == False:
            maps[dx+1][dy] = min(maps[dx+1][dy], maps[dx][dy] + 1)
            visited[dx+1][dy] = True
            queue.append((dx + 1, dy))
        if dx - 1 >= 0 and graph[dx-1][dy] == 1 and visited[dx-1][dy] == False:
            maps[dx-1][dy] = min(maps[dx-1][dy], maps[dx][dy] + 1)
            visited[dx-1][dy] = True
            queue.append((dx - 1, dy))
        if dy + 1 < len(graph[0]) and graph[dx][dy+1] == 1 and visited[dx][dy+1] == False:
            maps[dx][dy+1] = min(maps[dx][dy+1], maps[dx][dy] + 1)
            visited[dx][dy+1] = True
            queue.append((dx, dy + 1))
        if dy - 1 >= 0 and graph[dx][dy-1] == 1 and visited[dx][dy-1] == False:
            maps[dx][dy-1] = min(maps[dx][dy-1], maps[dx][dy] + 1)
            visited[dx][dy-1] = True
            queue.append((dx, dy - 1))

n, m = map(int, input().split())
graph = []
for _ in range(n):
    string = input().strip()
    str_list = [int(s) for s in string]
    graph.append(str_list)

infinite = float('INF')
maps = [[infinite for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
maps[0][0] = 1

bfs(graph, 0, 0, maps, visited)
print(maps[n-1][m-1])