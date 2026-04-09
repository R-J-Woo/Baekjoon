from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001

queue = deque()
queue.append((N, 0))
visited[N] = True

while queue:
    node, count = queue.popleft()
    if node == K:
        print(count)
        break

    if 0 <= node + 1 <= 100000 and not visited[node + 1]:
        queue.append((node + 1, count + 1))
        visited[node + 1] = True
    if 0 <= node - 1 <= 100000 and not visited[node - 1]:
        queue.append((node - 1, count + 1))
        visited[node - 1] = True
    if 0 <= node * 2 <= 100000 and not visited[node * 2]:
        queue.append((node * 2, count + 1))
        visited[node * 2] = True