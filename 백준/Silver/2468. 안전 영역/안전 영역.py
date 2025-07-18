import copy
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, x, y, visited, height):
    visited[x][y] = True

    if x > 0 and visited[x-1][y] != True and graph[x-1][y] >= height:
        dfs(graph, x-1, y, visited, height)
    if x + 1 < len(graph) and visited[x+1][y] != True and graph[x+1][y] >= height:
        dfs(graph, x+1, y, visited, height)
    if y > 0 and visited[x][y-1] != True and graph[x][y-1] >= height:
        dfs(graph, x, y-1, visited, height)
    if y + 1 < len(graph) and visited[x][y+1] != True and graph[x][y+1] >= height:
        dfs(graph, x, y+1, visited, height)

n = int(input())
heights = []
for _ in range(n):
    heights.append(list(map(int, input().split())))

visited = [[False] * (n) for _ in range(n)]
max_count = 0
max_height = 0
for height in range(0, 101):
    count = 0
    temp_heights = copy.deepcopy(heights)
    temp_visited = copy.deepcopy(visited)
    
    for x in range(n):
        for y in range(n):
            if temp_heights[x][y] < height or temp_visited[x][y] == True:
                continue

            dfs(temp_heights, x, y, temp_visited, height)
            count += 1

    if count > max_count:
        max_height = height
    max_count = max(max_count, count)


print(max_count)