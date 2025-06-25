# 1/1 -> 합 2
# 2/1 1/2 -> 합 3
# 3/1 2/2 1/3 -> 합 4
# 아이디어: 몇번째 대각선인지 확인하고, 그 줄에서 몇번째 인지 계산후 값 출력

import sys
input = sys.stdin.readline

x = int(input())

# 몇번째 대각선 줄인지 찾기
line = 1
while x > line:
    x -= line
    line += 1

# 해당 줄이 짝수 번째 줄인지 홀수번째 줄인지 확인
if line % 2 == 0:
    # 짝수번째라면 오른쪽에서 왼쪽
    a = x
    b = line + 1 -x
else:
    # 홀수번째라면 왼쪽에서 오른쪽
    a = line + 1 -x
    b = x

print(str(a) + '/' + str(b))