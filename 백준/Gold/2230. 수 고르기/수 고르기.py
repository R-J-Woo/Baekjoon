n, m = map(int, input().split())

num_list = [int(input()) for _ in range(n)]

# 오름차순 정렬
num_list.sort()

answer = float('inf')
start, end = 0, 0
while start < n and end < n:
    diff = num_list[end] - num_list[start]
    if diff < m:
        end += 1
    else:
        answer = min(answer, diff)
        start += 1

print(answer)