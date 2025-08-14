import sys
input = sys.stdin.readline

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(maps, x, y, visited, house):
    visited[x][y] = house
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and\
            maps[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(maps, nx, ny, visited, house)

visited = [[0] * n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == 0: # 아직 방문하지 않은 곳이라면 dfs 진행\
            count += 1
            dfs(maps, i, j, visited, count)
            
result = []
for k in range(1, count + 1):
    c = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == k:
                c += 1

    result.append(c)

print(count)
result.sort()
for r in result:
    print(r)