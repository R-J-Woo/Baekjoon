from collections import deque

# 동전이 밖으로 떨어졌는지 아닌지 체크하는 함수
def in_board(board, x, y):
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    else:
        return False

def bfs(graph, coins, visited):
    queue = deque()
    x1, y1 = coins[0]
    x2, y2 = coins[1]
    queue.append((x1, y1, x2, y2, 0))
    visited[x1][y1][x2][y2] = True

    while queue:
        x1, y1, x2, y2, count = queue.popleft()

        if count >= 10:
            return -1
        
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            # 밖으로 떨어졌는지 체크
            out1 = in_board(graph, nx1, ny1)
            out2 = in_board(graph, nx2, ny2)

            # 둘 중 하나만 떨어졌으면 정답
            if (out1 and not out2) or (not out1 and out2):
                return count + 1
            
            # 둘 다 떨어지면 무시
            if not out1 and not out2:
                continue

            # 벽이면 이동 X
            if out1 and board[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if out2 and board[nx2][ny2] == '#':
                nx2, ny2 = x2, y2

            if not visited[nx1][ny1][nx2][ny2]:
                visited[nx1][ny1][nx2][ny2] = True
                queue.append((nx1, ny1, nx2, ny2, count+1))

    return -1


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 동전 위치 찾기
coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
result = bfs(board, coins, visited)

print(result)