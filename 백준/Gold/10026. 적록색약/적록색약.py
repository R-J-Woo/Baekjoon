# 아이디어: 깊이 우선 탐색 (DFS) 알고리즘 사용

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input().strip()))

def dfs(maps, x, y, visited, flag):
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 적록색약 X
            if flag == 0 and maps[x][y] == maps[nx][ny]:
                dfs(maps, nx, ny, visited, flag)
            # 적록색약 O
            elif flag == 1 and (maps[x][y] == maps[nx][ny] or \
                    (maps[x][y] == 'R' and maps[nx][ny] == 'G') or 
                    (maps[x][y] == 'G' and maps[nx][ny] == 'R')):
                dfs(maps, nx, ny, visited, flag)

# 적록색약이 아닌 경우
result = []
count1 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count1 += 1
            dfs(maps, i, j, visited, 0)

result.append(count1)

# 적록색약인 경우
count2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count2 += 1
            dfs(maps, i, j, visited, 1)

result.append(count2)

print(' '.join(str(count) for count in result))