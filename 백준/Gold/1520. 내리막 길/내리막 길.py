# 아이디어: DFS + 메모이제이션 (Top-down DP)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 메모이제이션용 DP 테이블
dp = [[-1] * n for _ in range(m)]

def dfs(x, y):
    # 도착지에 도달하면 경로 1개
    if x == m - 1 and y == n - 1:
        return 1

    # 이미 방문해서 계산된 경우
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0  # 초기화 후 탐색 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] < maps[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))
