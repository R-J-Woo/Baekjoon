from collections import deque

def bfs(S, T):
    queue = deque()
    queue.append((S, T, 0))

    while queue:
        S, T, count = queue.popleft()

        if S == T:
            return count
        
        if S * 2 <= T + 3:
            queue.append((S * 2, T + 3, count + 1))
        
        if S + 1 <= T:
            queue.append((S + 1, T, count + 1))


C = int(input())

for _ in range(C):
    S, T = map(int, input().split())
    result = bfs(S, T)

    print(result)