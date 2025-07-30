from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

prices = []
weights = []

for _ in range(n): # O(N)
    prices.append(int(input()))

for _ in range(m): # O(M)
    weights.append(int(input()))

park = [0] * n
queue = deque()
result = 0
for _ in range(2 * m):
    car = int(input())

    if car < 0: # 주차장에서 나가기
        idx = park.index(abs(car)) # 주차된 위치 찾기: O(N)
        park[idx] = 0 # 위치 비우기

        if len(queue) > 0: # 대기 차량이 있으면 주차함
            idx = park.index(0) # 빈 주차공간 찾기: O(N)
            newCar = queue.popleft()
            park[idx] = newCar
            result += weights[newCar - 1] * prices[idx]
        continue

    if 0 not in park: # 주차 공간이 없으면
        queue.append(car)
    else:
        idx = park.index(0) # 빈 주차공간 찾기: O(N)
        park[idx] = car
        result += weights[car - 1] * prices[idx]

print(result)