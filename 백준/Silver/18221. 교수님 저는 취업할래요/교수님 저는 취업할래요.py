N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

pi, pj = 0, 0
si, sj = 0, 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 5:
            pi, pj = i, j
        elif graph[i][j] == 2:
            si, sj = i, j

student = 0
for i in range(min(pi, si), max(pi, si) + 1):
    for j in range(min(pj, sj), max(pj, sj) + 1):
        if graph[i][j] == 1:
            student += 1

distance = abs(pi - si) ** 2 + abs(pj - sj) ** 2
if distance >= 25 and student >= 3:
    print(1)
else:
    print(0)