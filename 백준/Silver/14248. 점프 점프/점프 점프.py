from collections import deque

n = int(input())
Ai = list(map(int, input().split()))
s = int(input())

visited = [False] * n

queue = deque()
queue.append((s - 1))

count = 1
while queue:
    node = queue.popleft()
    dist = Ai[node]
    
    left, right = node - dist, node + dist

    if left >= 0 and not visited[left]:
        visited[left] = True
        queue.append((left))
        count += 1

    if right < n and not visited[right]:
        visited[right] = True
        queue.append((right))
        count += 1


print(count)