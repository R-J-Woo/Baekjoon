import sys
input = sys.stdin.readline

N = int(input())
days = [0] * 366
for _ in range(N):
    s, e = map(int, input().split())
    for d in range(s, e + 1):
        days[d] += 1

result = 0
width = 0
height = 0

for d in range(1, 366):
    if days[d] > 0:
        width += 1
        height = max(height, days[d])
    else:
        result += width * height
        width = 0
        height = 0

result += width * height
print(result)