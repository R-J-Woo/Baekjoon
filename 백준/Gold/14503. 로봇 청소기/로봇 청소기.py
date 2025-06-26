import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 0은 아직 청소안한 칸, 1은 벽, 2는 청소를 마친 칸
count = 0
while True:
    # 1. 현재 칸이 청소되지 않은 경우, 현재 칸을 청소
    if maps[r][c] == 0:
        count += 1
        maps[r][c] = 2
    
    # 2. 주변 4칸 중 청소되지 않은 칸이 없는 경우
    if maps[r-1][c] != 0 and maps[r][c+1] != 0 and maps[r+1][c] != 0 and maps[r][c-1] != 0:
        # 2-1. 1칸 후진이 가능하면 후진
        if d == 0:
            if maps[r+1][c] != 1:
                r += 1
            else:
                break
        elif d == 1:
            if maps[r][c-1] != 1:
                c -= 1
            else:
                break
        elif d == 2:
            if maps[r-1][c] != 1:
                r -= 1
            else:
                break
        elif d == 3:
            if maps[r][c+1] != 1:
                c += 1
            else:
                break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        # 3-1. 반시계 방향으로 90* 회전
        if d == 0:
            d = 3
        elif d == 1:
            d = 0
        elif d == 2:
            d = 1
        elif d == 3:
            d = 2

        # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한칸 전진
        if d == 0 and maps[r-1][c] == 0:
            r -= 1
        elif d == 1 and maps[r][c+1] == 0:
            c += 1
        elif d == 2 and maps[r+1][c] == 0:
            r += 1
        elif d == 3 and maps[r][c-1] == 0:
            c -= 1

print(count)