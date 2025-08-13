from collections import deque

n = int(input())
queue = deque()
for i in range(1, n + 1):
    queue.append(i)

count = 0
result = []
while len(queue) > 1:
    count += 1
    if count % 2 != 0: # 홀수 번째는 그냥 버림
        num = queue.popleft()
        result.append(num)
    else:
        num = queue.popleft()
        queue.append(num)

num = queue.popleft()
result.append(num)
print(' '.join(str(num) for num in result))