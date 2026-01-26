l = int(input())
commands = list(input())

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = [['#'] * 101 for _ in range(101)]
x, y = 50, 50 # 현재 위치
graph[x][y] = '.'
direction = 2 # 시작은 아래를 보고 있음
for c in commands:
    if c == 'R':
        if direction < 3:
            direction += 1
        else:
            direction = 0
    elif c == 'L':
        if direction == 0:
            direction = 3
        else:
            direction -= 1
    elif c == 'F':
        x += dx[direction]
        y += dy[direction]
        graph[x][y] = '.'

dots = []
for i in range(101):
    for j in range(101):
        if graph[i][j] == '.':
            dots.append((i, j))

min_r = min(i for i, j in dots)
max_r = max(i for i, j in dots)
min_c = min(j for i, j in dots)
max_c = max(j for i, j in dots)

for i in range(min_r, max_r + 1):
    print(''.join(graph[i][min_c:max_c + 1]))
