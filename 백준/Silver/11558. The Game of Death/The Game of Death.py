import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    
    N = int(input())
    graph = [0] + [int(input()) for _ in range(N)]

    current = 1
    result = 0
    visited = [False] * (N + 1)
    while True:
        if current == N:
            print(result)
            break

        if visited[current]:
            print(0)
            break

        visited[current] = True
        result += 1
        current = graph[current]
