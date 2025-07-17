# 아이디어: 큐를 사용하여 뱀의 몸을 표현
# 큐에 들어있는 좌표는 뱀의 몸이 차지하는 칸임
# 이동을 하면 새롭게 이동하는 머리는 추가하고, 이동하는 뒤 꼬리는 삭제함
# 큐에 동일한 좌표가 두개 이상 있다면 자기 몸과 부딪히는 것으로 판단

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
maps = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k): # O(K)
    x, y = map(int, input().split())
    maps[x-1][y-1] = 1

l = int(input())
commands = deque()
for _ in range(l): # O(L)
    x, c = input().split()
    x = int(x)
    commands.append((x, c))

# 방향: 위 우 아래 좌
dX = [-1, 0, 1, 0]
dY = [0, 1, 0, -1]
dir = 1

x, y = 0, 0 # 머리 기준 위치
snake = deque() # 뱀이 차지하는 칸
snake.append((x, y))
time = 0 # 소요 시간
while True:
    if commands and time == commands[0][0]:
        _, c2 = commands.popleft()
        if c2 == 'L':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4

    time += 1
    x += dX[dir]
    y += dY[dir]

    # 벽 충돌 or 자기 몸과 충돌
    if x < 0 or x >= n or y < 0 or y >= n or (x, y) in snake:
        break

    # 사과가 있으면 머리만 이동
    if maps[x][y] == 1:
        maps[x][y] = 0
        snake.append((x, y))
    else:
        snake.append((x, y))
        snake.popleft()

print(time)