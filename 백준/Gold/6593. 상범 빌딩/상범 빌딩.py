from collections import deque
import sys
input = sys.stdin.readline

def bfs(building, start, end, visited, L, R, C):
    queue = deque()
    c, a, b = start
    queue.append((c, a, b, 0))
    visited[c][a][b] = True

    dz = [0, 0, 0, 0, 1, -1]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]

    while queue:
        z, x, y, dist = queue.popleft()
        
        if (z, x, y) == end:
            return dist
        
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny, dist + 1))
        

while True:
    L, R, C = map(int, input().split())
    
    if L == 0 and R == 0 and C == 0:
        exit()


    building = []
    start = ()
    end = ()
    for z in range(L):
        floor = []
        for x in range(R):
            row = list(input().strip())
            if 'S' in row or 'E' in row:
                for y in range(C):
                    if row[y] == 'S':
                        start = (z, x, y)
                    elif row[y] == 'E':
                        end = (z, x, y)

            floor.append(row)

        building.append(floor)
        input() # 층 사이 빈줄
    

    # 3차원 visited
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    result = bfs(building, start, end, visited, L, R, C)

    if result is None:
        print("Trapped!")
    else:
        print("Escaped in " + str(result) + " minute(s).")
