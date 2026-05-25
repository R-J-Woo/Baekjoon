from collections import deque

def bfs(board, x, y, visited):
    queue = deque()
    queue.append((x, y, 0)) # x좌표, y좌표, 이동거리
    visited[x][y] = True
    
    distance = -1
    while queue:
        x, y, count = queue.popleft()
        
        # 종료 조건 -> G에 도착했을 경우
        if board[x][y] == 'G':
            distance = count
            break
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            
            nx, ny = 0, 0
            
            # 가장자리나 장애물에 부딪힐 때까지 이동
            for i in range(1, 100):
                tx = x + i * dx
                ty = y + i * dy
                
                if tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0]) or board[tx][ty] == 'D':
                    nx = tx - dx
                    ny = ty - dy
                    break
                    
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
                
            
    return distance


def solution(board):
    answer = 0
    
    # R의 위치 찾기
    R = (0, 0)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                R = (i, j)
                break
                
    # bfs로 탐색
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    distance = bfs(board, R[0], R[1], visited)
    
    return distance