import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n): # O(N)
    line.append(list(map(int, input().split())))

# 시작점 기준 정렬, 같으면 끝점 기준 정렬
line.sort(key=lambda x: (x[0], x[1]))

last = -10**9 
result = 0

for l in line:
    if l[0] > last:  # 새 구간 시작
        result += (l[1] - l[0])
        last = l[1]
    else:  # 겹치는 구간
        if l[1] > last:
            result += (l[1] - last)
            last = l[1]
print(result)