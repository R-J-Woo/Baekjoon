from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    festival = tuple(map(int, input().split()))

    queue = deque()
    queue.append(home)
    visited = [False] * n
    happy = False

    while queue:
        x, y = queue.popleft()

        if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:
            happy = True
            break

        for i in range(n):
            if not visited[i]:
                sx, sy = stores[i]
                if abs(sx - x) + abs(sy - y) <= 1000:
                    visited[i] = True
                    queue.append((sx, sy))

    if happy:
        print("happy")
    else:
        print("sad")