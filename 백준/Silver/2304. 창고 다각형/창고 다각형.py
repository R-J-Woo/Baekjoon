import sys
input = sys.stdin.readline

n = int(input())
container = [0] * 1001

for _ in range(n):
    l, h = map(int, input().split())
    container[l] = h

max_h = max(container)
max_idx = container.index(max_h)

area = 0

# 왼쪽에서 최대 높이까지
highest = 0
for i in range(max_idx+1):
    highest = max(highest, container[i])
    area += highest

# 오른쪽에서 최대 높이까지
highest = 0
for i in range(1000, max_idx, -1):
    highest = max(highest, container[i])
    area += highest

print(area)
