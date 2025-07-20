# 아이디어: bfs 사용
# 우선 초기에 익은 토마토는 0일차로 설정
# bfs를 반복하면서 아직 익지 않은 토마토는 그 이전 토마토의 익은 일 수의 +1을 해줌
# 총 걸린 일수를 출력

from collections import deque
import sys
input = sys.stdin.readline

def bfs(box):
    queue = deque()
    # 첫날 익은 토마토의 위치 구하기 -> O(N^2)
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 1:
                queue.append((i, j, 0)) # 행, 열, 익은 날짜 저장

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # bfs로 박스 탐색
    day = 0
    while queue:
        x, y, tempDay = queue.popleft()
        if day != tempDay:
            day = tempDay
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 박스를 벗어나면 패스
            if nx < 0 or nx >= len(box) or ny < 0 or ny >= len(box[0]):
                continue

            # 토마토 없는 칸은 패스
            if box[nx][ny] == -1:
                continue

            # 토마토가 이미 익없으면 패스
            if box[nx][ny] == 1:
                continue

            # 이전 칸 토마토가 익은 날짜에 +1을 해서 저장
            queue.append((nx, ny, tempDay + 1))
            box[nx][ny] = 1

    # 안 익은 토마토가 있는지 확인
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 0:
                return -1
            
    return day



m, n = map(int, input().split()) # n: 행, m: 열
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

total_day = bfs(box)

print(total_day)