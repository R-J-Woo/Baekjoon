# 아이디어: 그리디 알고리즘
# 일수를 역순으로 돌면서 해당 날짜에 가능한 과제 중 가장 큰 점수를 실행

import sys
input = sys.stdin.readline

n = int(input())
hw = []
for _ in range(n):
    hw.append(list(map(int, input().split())))

hw.sort() # 일수가 가장 큰 순서대로 정렬
canHW = [] # 해당 일수에 가능한 과제를 저장할 리스트
result = 0

# 마지막 일수부터 가장 처음 일수까지 반복
for date in range(n, 0, -1):
    while hw and hw[-1][0] >= date: # 해당 날짜에 수행할 수 있는 과제점수를 리스트에 저장
        canHW.append(hw.pop()[1])
    # 해당 날짜에 수행할 수 있는 과제가 있다면
    if canHW:
        canHW.sort()
        result += canHW.pop()

print(result)