from collections import deque


def bfs(graph, a, b, target, visited):
    queue = deque()
    queue.append((a, b, 0))
    visited[a][b] = True

    dx = [-1, 1, 0, 0, 1, -1]
    dy = [0, 0, -1, 1, -1, 1]

    while queue:
        x, y, move = queue.popleft()
        
        if graph[x][y] == target:
            return x, y, move
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]) and not visited[nx][ny]:
                queue.append((nx, ny, move + 1))
                visited[nx][ny] = True

def find_locate(graph, target):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == target:
                return i, j


graph = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
         ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
         ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]

T = int(input())
for _ in range(T):
    string = input()
    time = 0

    a, b = find_locate(graph, string[0])
    for i in range(len(string)):    
        visited = [[False] * len(graph[i]) for i in range(len(graph))]
        
        # 누르고 떼는 시간 1초
        time += 1
        
        # 버튼 옮기는 시간
        if i != (len(string) - 1):
            a, b, move = bfs(graph, a, b, string[i + 1], visited)
            time += 2 * move

    print(time)