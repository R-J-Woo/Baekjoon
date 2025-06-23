# 아이디어: 작은 수부터 정렬하면 최소값이 나오지 않을까
# 우선순위큐 사용

import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    num = int(input())
    heapq.heappush(cards, num)

count = 0
while len(cards) > 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    temp = num1 + num2
    count += temp
    heapq.heappush(cards, temp)

print(count)