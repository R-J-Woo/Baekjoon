import sys
input = sys.stdin.readline

n, m = map(int, input().split())
square = []
for _ in range(n):
    square.append(list(input().strip()))

area = 1 # 길이가 1일때는 항상 꼭짓점의 수가 같으므로, 1에서의 크기 1은 보장
for length in range(1, min(n, m)): # 정사각형 한 변의 길이
    for i in range(n - length): # x 좌표
        for j in range(m - length): # y 좌표
            # 네 꼭짓점이 모두 동일하다면
            if square[i][j] == square[i][j+length]\
                  == square[i+length][j] == square[i+length][j+length]:
                area = max(area, (length + 1) ** 2)

print(area)