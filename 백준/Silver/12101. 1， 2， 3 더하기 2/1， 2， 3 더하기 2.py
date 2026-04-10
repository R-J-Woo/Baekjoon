from collections import deque

N, K = map(int, input().split())

queue = deque()
for i in range(1, 4):
    temp = []
    temp.append(i)
    queue.append(temp)

result = []
while queue:
    num_list = queue.popleft()
    total = sum(num_list)

    if total == N:
        result.append(num_list)
        continue

    for i in range(1, 4):  # 1,2,3만 가능
        if total + i <= N:
            queue.append(num_list + [i])

result.sort()

if len(result) < K:
    print(-1)
else:
    print('+'.join(map(str, result[K-1])))