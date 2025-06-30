# 아이디어: 그래프 탐색을 전체적으로 진행한 뒤, 끝났을 때 끝 점에 방문을 했는지 판단

def dfs(game_map, n, x, y, visited):
    # 현재 노드를 방문 처리
    visited[x][y] = True

    # 현재 노드에서 갈 수 있는 점을 방문
    distance = game_map[x][y]
    if x + distance < n and not visited[x+distance][y]:
        dfs(game_map, n, x + distance, y, visited)

    if y + distance < n and not visited[x][y+distance]:
        dfs(game_map, n, x, y + distance, visited)

n = int(input())

game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

visited = [[False] * n for i in range(n)]

dfs(game_map, n, 0, 0, visited)

# 끝 점에 방문하지 않았다면
if not visited[n - 1][n - 1]:
    print("Hing")
else:
    print("HaruHaru")