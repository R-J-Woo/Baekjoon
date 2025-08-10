# 아이디어: 넓이에 포함되지 않는 작은 사각형은
# 가장 긴 가로, 세로 변의 앞뒤 변 길이를 이용한다

k = int(input())
command = []
max_x, max_y = 0, 0
max_x_idx, max_y_idx = 0, 0

for i in range(6):
    d, length = map(int, input().split())
    command.append((d, length))
    if d in (1, 2):  # 동, 서 → 가로
        if length > max_x:
            max_x = length
            max_x_idx = i
    elif d in (3, 4):  # 남, 북 → 세로
        if length > max_y:
            max_y = length
            max_y_idx = i

# 작은 사각형의 변 구하기
small_w = abs(command[(max_y_idx - 1) % 6][1] - command[(max_y_idx + 1) % 6][1])
small_h = abs(command[(max_x_idx - 1) % 6][1] - command[(max_x_idx + 1) % 6][1])

# 전체 면적 - 작은 사각형 면적
area = (max_x * max_y) - (small_w * small_h)
print(area * k)
