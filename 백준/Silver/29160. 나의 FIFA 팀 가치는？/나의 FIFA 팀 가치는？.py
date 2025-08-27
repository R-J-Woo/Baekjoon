# 아이디어: 우선순위큐 알고리즘 이용

import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
player = [[] for _ in range(12)]
for _ in range(n):
    p, w = map(int, input().split())
    heapq.heappush(player[p], -w) # 내림차순을 위해 - 붙여서 삽입

for _ in range(k):
    for i in range(1, 12):
        # 선수가 없으면 패스
        if not player[i]:
            continue
        p = -heapq.heappop(player[i])
        if p > 0:
            p -= 1
        heapq.heappush(player[i], -p)



result = 0
for i in range(1, 12):
    if player[i]:
        result += -heapq.heappop(player[i])

print(result)