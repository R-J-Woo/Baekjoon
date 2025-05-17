import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

max_h = 0
start = 0
end = max(heights)
result = 0
while start <= end:
    total = 0 # 가져갈 수 있는 나무 총길이
    h = (start + end) // 2 # 절단기 높이
    for height in heights:
        if height > h:
            total += height - h

    if total >= m: # 가져갈 수 있는 총길이가 m보다 크다면
        result = h
        start = h + 1
    else:
        end = h - 1

print(result)