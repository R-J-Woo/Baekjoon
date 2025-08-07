import heapq

n, m = map(int, input().split())
tempA = list(map(int, input().split()))

A = []
for item in tempA:
    heapq.heappush(A, item)

for _ in range(m):
    card1 = heapq.heappop(A)
    card2 = heapq.heappop(A)
    sum = card1 + card2
    heapq.heappush(A, sum)
    heapq.heappush(A, sum)

sum = 0
while A:
    sum += heapq.heappop(A)

print(sum)