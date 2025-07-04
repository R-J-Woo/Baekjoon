# 아이디어: 이전까지 가장 적은 비용으로 그렸던 집에서 현재의 값을 더해줌
# 다만, 이전 마지막으로 칠했던 색이 현재의 색과 달라야 함

import sys
input = sys.stdin.readline

n = int(input())
RGB = []
for _ in range(n):
    RGB.append(list(map(int, input().split())))

for i in range(1, len(RGB)):
    RGB[i][0] = min(RGB[i-1][1] + RGB[i][0], RGB[i-1][2] + RGB[i][0])
    RGB[i][1] = min(RGB[i-1][0] + RGB[i][1], RGB[i-1][2] + RGB[i][1])
    RGB[i][2] = min(RGB[i-1][0] + RGB[i][2], RGB[i-1][1] + RGB[i][2])

print(min(RGB[-1]))