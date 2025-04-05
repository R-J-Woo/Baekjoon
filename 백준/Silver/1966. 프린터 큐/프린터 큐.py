from collections import deque

count = int(input())

for _ in range(count):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    queue = deque([(i, p) for i, p in enumerate(importance)])
    count = 0

    while queue:
        current = queue.popleft()

        # 현재 문서보다 중요한 문서가 있다면
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                print(count)
                break