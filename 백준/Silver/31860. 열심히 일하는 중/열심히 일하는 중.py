import heapq

n, m, k = map(int, input().split())
importants = []
for _ in range(n):
    heapq.heappush(importants, -int(input()))

happy = []
today = 0
count = 0
while True:
    work = -heapq.heappop(importants)
    if work <= k:
        break

    count += 1
    today = (today // 2) + work
    happy.append(today)
    work -= m
    heapq.heappush(importants, -work)

print(count)
for h in happy:
    print(h)