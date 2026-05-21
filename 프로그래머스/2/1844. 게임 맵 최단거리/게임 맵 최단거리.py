from collections import deque

def solution(maps):
    
    row = len(maps)
    col = len(maps[0])
    queue = deque()
    queue.append((0, 0, 1)) # x좌표, y좌표, 칸 개수
    
    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = -1
    while queue:
        x, y, count = queue.popleft()
        
        # 상대팀 진영에 도착
        if x == row - 1 and y == col - 1:
            answer = count
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
        
    return answer
        