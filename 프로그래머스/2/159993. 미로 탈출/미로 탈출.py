from collections import deque

def bfs(maps, start, target, visited):
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    
    result = -1 # 시작에서 도착지까지의 거리
    
    while queue:
        x, y, distance = queue.popleft()
        
        if (x, y) == target:
            result = distance
            break
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
                
    return result


def solution(maps):
    answer = 0
    start = (0, 0) # 시작 위치
    lever = (0, 0) # 레버 위치
    exit = (0, 0)  # 출구 위치
    
    # 시작지, 레버, 출구 위치 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
            elif maps[i][j] == 'S':
                start = (i, j)
                
    # 출발지부터 레버까지 탐색
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    distance = bfs(maps, start, lever, visited)
    
    # 출발지부터 레버까지 갈 수 없다면
    if distance == -1:
        return -1
    
    answer += distance
    
    # 레버부터 도착지까지 탐색
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    distance = bfs(maps, lever, exit, visited)
    
    # 레버부터 도착지까지 갈 수 없다면
    if distance == -1:
        return -1

    answer += distance
        
    return answer