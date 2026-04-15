from collections import deque

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y, graph[x][y])) # x좌표, y좌표, 현재 숫자

    result = set()
    while queue:
        x, y, num = queue.popleft()
        if len(num) == 6:
            result.add(num)
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                new_num = num + graph[nx][ny]
                queue.append((nx, ny, new_num))

    return result


board = [list(input().split()) for _ in range(5)]

result = set()
for i in range(5):
    for j in range(5):
        new_result = bfs(board, i, j)
        result = result | new_result

print(len(result))
