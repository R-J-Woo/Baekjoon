# 아이디어: 우선순위 큐 알고리즘 이용

import heapq
import sys
input = sys.stdin.readline

n, h, t = map(int, input().split())
titan = []
for _ in range(n):
    height = int(input())
    heapq.heappush(titan, -height) # 내림차순을 위해 -을 붙여서 삽입

count = 0 # 뿅망치 사용 횟수
for _ in range(t):
    p = -heapq.heappop(titan)
    if p < h:
        heapq.heappush(titan, -p)
        break
    count += 1
    if p > 1:
        p //= 2
    heapq.heappush(titan, -p)

max_height = -heapq.heappop(titan)
if max_height < h:
    print("YES")
    print(count)
else:
    print("NO")
    print(max_height)