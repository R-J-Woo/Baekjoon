import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
block = {}
min_value = 300
max_value = 0

# 시간 복잡도: O(n^2) -> 250000
for _ in range(n):
    row = list(map(int, input().split()))
    for value in row:
        if value in block:
            block[value] += 1
        else:
            block[value] = 1

time_cost = float('inf') # 걸리는 시간
height = 0 # 땅의 높이
for h in range(257): # key = 기준 높이
    time_temp = 0
    block_cost = 0
    for i in block:
        if h < i: # 블록 높이가 높으면 제거 -> 2초
            time_temp += (i - h) * block[i] * 2
            block_cost -= (i - h) * block[i]
        elif h > i: # 블록 높이가 낮으면 하나 놓기 -> 1초
            time_temp += (h - i) * block[i]
            block_cost += (h - i) * block[i]
        else:
            continue

    if block_cost > b: # 블록 소모량이 입력한 b 값보다 많다면 패스
        continue

    if time_temp <= time_cost:
        time_cost = time_temp
        if height < h:
            height = h

print(time_cost, height)