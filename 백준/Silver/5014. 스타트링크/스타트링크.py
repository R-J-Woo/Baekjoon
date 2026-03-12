from collections import deque

def dfs(height, start, target, visited, up, down):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    result = 10000000
    while queue:
        floor, move = queue.popleft()

        if floor == target:
            result = min(result, move)

        nxt1 = floor + up
        nxt2 = floor - down
        if nxt1 <= height and not visited[nxt1]:
            visited[nxt1] = True
            queue.append((nxt1, move + 1))
        
        if nxt2 > 0 and not visited[nxt2]:
            visited[nxt2] = True
            queue.append((nxt2, move + 1))

    return result


F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)
result = dfs(F, S, G, visited, U, D)

if result == 10000000:
    print("use the stairs")
else:
    print(result)