import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]

# 1. 누적합 배열 생성 (1-indexed)
prefix = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = (
            numbers[i-1][j-1]
            + prefix[i-1][j]
            + prefix[i][j-1]
            - prefix[i-1][j-1]
        )

# 2. 쿼리 처리
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())

    result = (
        prefix[x][y]
        - prefix[i-1][y]
        - prefix[x][j-1]
        + prefix[i-1][j-1]
    )

    print(result)