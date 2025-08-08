from collections import deque

n, k = map(int, input().split())

queue = deque()
for i in range(1, n + 1):
    queue.append(i)

count = 0
result = []
while len(result) < n:
    num = queue.popleft()
    if num == 0:
        continue

    count += 1
    if count % k == 0:
        result.append(num)
        queue.append(0)
    else:
        queue.append(num)

print("<" + ', '.join(str(num) for num in result) + ">")