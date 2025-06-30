import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(maps, x, y, visited):
    # 현재 노드 방문 처리
    visited[x][y] = True

    # 현재 노드와 연결된 다른 노드 방문
    if x - 1 >= 0 and maps[x-1][y] == 1 and visited[x-1][y] == False:
        dfs(maps, x-1, y, visited)
    if x + 1 < len(maps) and maps[x+1][y] == 1 and visited[x+1][y] == False:
        dfs(maps, x+1, y, visited)
    if y - 1 >= 0 and maps[x][y-1] == 1 and visited[x][y-1] == False:
        dfs(maps, x, y-1, visited)
    if y + 1 < len(maps[0]) and maps[x][y+1] == 1 and visited[x][y+1] == False:
        dfs(maps, x, y+1, visited)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    maps = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            # 노드가 1인데 아직 방문안한 노드라면
            if maps[i][j] == 1 and visited[i][j] == False:
                dfs(maps, i, j, visited)
                count += 1

    print(count)