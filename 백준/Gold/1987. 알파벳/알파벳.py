import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [False] * 26  # 알파벳 방문 여부
max_count = 0

def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            idx = ord(maps[nx][ny]) - ord('A')
            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, count + 1)
                visited[idx] = False  # 백트래킹

# 시작 위치 방문 처리
visited[ord(maps[0][0]) - ord('A')] = True
dfs(0, 0, 1)
print(max_count)
