from collections import deque

field = []
for _ in range(12):
    field.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 너비 우선 탐색
def bfs(i, j, color, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    result = [] # 터지게 되는 노드 저장
    result.append([i, j])

    while queue:
        (x, y) = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # 동일한 색이면 연쇄에 추가
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == False\
                and field[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = True
                result.append([nx, ny])

    return result


result = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    any_boom = False

    # 터짐
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                nodes = bfs(i, j, field[i][j], visited)
                if len(nodes) >= 4:
                    any_boom = True
                    for node in nodes:
                        field[node[0]][node[1]] = '.'

    # 터진 것이 없다면 종료
    if not any_boom:
        break

    result += 1

    # 중력: 각 열을 압축해서 바닥부터 채움 (한 번에 완전히 떨어짐)
    for j in range(6):
        new_col = ['.'] * 12
        idx = 11
        for i in range(11, -1, -1):
            if field[i][j] != '.':
                new_col[idx] = field[i][j]
                idx -= 1
        for i in range(12):
            field[i][j] = new_col[i]

print(result)