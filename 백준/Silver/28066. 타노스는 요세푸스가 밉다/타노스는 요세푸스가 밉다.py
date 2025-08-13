# 아이디어: 큐를 이용

from collections import deque

queue = deque()
n, k = map(int, input().split())
for i in range(1, n + 1):
    queue.append(i)

result = 0
while True:
    # 남아있는 청설모의 수가 k 보다 적으면
    if len(queue) < k:
        result = queue.popleft()
        break
    # 아니면 첫 번째 청설모는 살려두고 나머지는 제거
    else:
        num = queue.popleft()
        queue.append(num)
        for _ in range(k - 1):
            queue.popleft()

print(result)