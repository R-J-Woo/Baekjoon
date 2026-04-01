from collections import deque

def bfs(target, start, visited):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        num, count = queue.popleft()

        if num == target:
            return count

        if num * 2 <= target and not visited[num * 2]:
            queue.append((num * 2, count + 1))
            visited[num * 2] = True
        
        if num + 1 <= target and not visited[num + 1]:
            queue.append((num + 1, count + 1))
            visited[num + 1] = True


A, K = map(int, input().split())
visited = [False] * (K + 1)

print(bfs(K, A, visited))